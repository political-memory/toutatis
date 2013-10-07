# encoding: utf-8

import sys
from datetime import date, timedelta
from itertools import izip_longest

from django.core.management.base import BaseCommand
from django.db import transaction, reset_queries

from curating.models import CuratedProposalPart
from parltrack_meps.models import Group, MEP, CountryMEP
from parltrack_votes.models import ProposalPart

group_convertion_table = {
    "PPE": "EPP",
    "S&D": "SD",
    "Verts/ALE": "Greens/EFA",
}

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        a = 0
        total = ProposalPart.objects.count()
        #total = ProposalPart.objects.filter(datetime__gte=date(2013, 7, 1)).select_related('curatedproposalpart').count()
        #for proposal_part in ProposalPart.objects.filter(datetime__gte=date(2013, 7, 1)).select_related('curatedproposalpart'):
        for proposal_part in ProposalPart.objects.all().order_by('-datetime').select_related('curatedproposalpart', 'proposal'):
            with transaction.commit_on_success():
                a += 1
                b = 0
                fails = []

                if proposal_part.vote_set.filter(mep__isnull=False).count() == proposal_part.vote_set.count():
                    continue

                if not CuratedProposalPart.objects.filter(proposal_part=proposal_part):
                    proposal_part.curatedproposalpart = CuratedProposalPart(proposal_part=proposal_part)
                    proposal_part.curatedproposalpart.save()
                    for chunck in grouper(set([x.mep for x in CountryMEP.objects.filter(begin__lte=proposal_part.datetime.date(), end__gte=proposal_part.datetime.date() - timedelta(days=1))]), 100):
                        proposal_part.curatedproposalpart.meps.add(*filter(None, chunck))

                    proposal_part.curatedproposalpart.save()

                total_votes = proposal_part.vote_set.filter(mep__isnull=True).count()
                for vote in proposal_part.vote_set.filter(mep__isnull=True):
                    b += 1
                    raw_mep = vote.raw_mep.replace(u"ß", "SS").replace("`", "'").replace("*", "")

                    # the EP staff write or don't write their last last name
                    if raw_mep == "Vitkauskaite":
                        raw_mep = "VITKAUSKAITE BERNARD"
                    if raw_mep == "Mathieu":
                        raw_mep = "MATHIEU HOUILLON"
                    if raw_mep == "Jordan Cizelj":
                        raw_mep = "JORDAN"
                    if raw_mep == "Kleva":
                        raw_mep = u'KLEVA KEKU\u0160'
                    if raw_mep == "Savisaar":
                        raw_mep = "SAVISAAR-TOOMAST"
                    if raw_mep == u'Mork\u016bnait\u0117':
                        raw_mep = "MORKŪNAITĖ-MIKULĖNIENĖ"
                    if raw_mep == u'Paksas* Rossi':
                        raw_mep = "Paksas"
                    if raw_mep == u'Morin':
                        raw_mep = "MORIN-CHARTIER"
                    if raw_mep == u'Obiols i Germ\xe0':
                        raw_mep = "OBIOLS"
                    if raw_mep == u'Meyer Pleite':
                        raw_mep = "MEYER"
                    if raw_mep == u'Wojciechowski Bernard Piotr':
                        raw_mep = "WOJCIECHOWSKI"
                    if raw_mep == u'Hammerstein Mintz':
                        raw_mep = "HAMMERSTEIN"
                    if raw_mep == u'Ayuso Gonz\xe1lez':
                        raw_mep = "AYUSO"
                    if raw_mep == u'Galeote Quecedo':
                        raw_mep = "GALEOTE"
                    if raw_mep == u'Vidal-Quadras Roca':
                        raw_mep = "VIDAL-QUADRAS"
                    if raw_mep == u'Evans Jillian':
                        raw_mep = "EVANS Jill"
                    if raw_mep == u'Jordan amCizelj':
                        raw_mep = "Jordan Romana"
                    if raw_mep == u'Bern\xe1thn\xe9 Moh\xe1csi':
                        raw_mep = "MOHÁCSI"
                    if raw_mep == u'Martin David W.':
                        raw_mep = "Martin David"
                    if raw_mep == u'Evans Robert J.E.':
                        raw_mep = "Evans Robert"
                    if raw_mep == u'Romeva Rueda':
                        raw_mep = "ROMEVA i RUEDA"
                    if raw_mep == u'Badia Cutchet':
                        raw_mep = "BADIA i CUTCHET"
                    if raw_mep == u'Lambsdorff Graf':
                        raw_mep = "Graf LAMBSDORFF"

                    # special unicode char
                    if raw_mep in ("Rodriguez", "Perello Rodriguez"):
                        raw_mep = u'PERELL\xd3 RODR\xcdGUEZ'
                    if raw_mep == u'Sa\u010ffi':
                        raw_mep = u'SA\xcfFI'
                    if raw_mep in ('Grosset\xc3\xaate', u'Grosset\u0119te', u'Grossetete', 'Grosset\xc3\xaate'):
                        raw_mep = u'GROSSET\xcaTE'
                    if raw_mep == u'Patr\u0103o Neves':
                        raw_mep = "PATRÃO NEVES"
                    if raw_mep == u'Gauz\u010ds':
                        raw_mep = "GAUZÈS"
                    if raw_mep == u'Estar\u0155s Ferragut':
                        raw_mep = "ESTARÀS FERRAGUT"
                    if raw_mep in (u'Gr\u010dze', u'Greze'):
                        raw_mep = "GRÈZE"
                    if raw_mep == u'J\u0159rgensen':
                        raw_mep = "JØRGENSEN"
                    if raw_mep == u'S\u0159ndergaard':
                        raw_mep = "SØNDERGAARD"
                    if raw_mep in (u'Scott\u0155', u"Scotta'"):
                        raw_mep = "SCOTTÀ"
                    if raw_mep == u'Estaras Ferragut':
                        raw_mep = "ESTARÀS FERRAGUT"
                    if raw_mep == u'Haefner':
                        raw_mep = "HÄFNER"
                    if raw_mep == u'Jimenez-Becerril Barrio':
                        raw_mep = "JIMÉNEZ-BECERRIL BARRIO"
                    if raw_mep == u'Y\xe1\u0144ez-Barnuevo Garc\xeda':
                        raw_mep = "YÁÑEZ-BARNUEVO GARCÍA"
                    if raw_mep == u'Zappal\xe0':
                        raw_mep = "ZAPPALA'"
                    if raw_mep == u'Teychenne':
                        raw_mep = "TEYCHENNÉ"
                    if raw_mep == u'Henin':
                        raw_mep = "HÉNIN"
                    if raw_mep == u'Lefrancois':
                        raw_mep = "LEFRANÇOIS"
                    if raw_mep == u'Verges':
                        raw_mep = "VERGÈS"
                    if raw_mep == u'Foure':
                        raw_mep = "FOURÉ"
                    if raw_mep == u'Nicule\u015fcu':
                        raw_mep = "NICULESCU"
                    if raw_mep == u'Ya\xf1ez-Barnuevo Garc\xeda':
                        raw_mep = "YÁÑEZ-BARNUEVO GARCÍA"
                    if raw_mep == u'T\xeerle':
                        raw_mep = "ŢÎRLE"
                    if raw_mep == u'Poettering':
                        raw_mep = "PÖTTERING"
                    if raw_mep == u'Bad\xeda i Cutchet':
                        raw_mep = "BADIA i CUTCHET"
                    if raw_mep == u'RoG\xe1lski':
                        raw_mep = "ROGALSKI"
                    if raw_mep == u'Garc\xeda-MarG\xe1llo y Marfil':
                        raw_mep = "GARCÍA-MARGALLO Y MARFIL"
                    if raw_mep == u'Ku\u0161kis':
                        raw_mep = "KUŠĶIS"
                    if raw_mep == u'\u0160tastn\xfd':
                        raw_mep = "ŠŤASTNÝ"
                    if raw_mep == u'Stroz':
                        raw_mep = "STROŽ"
                    if raw_mep == u'Piks':
                        raw_mep = "PĪKS"
                    if raw_mep == u'Pek':
                        raw_mep = "PĘK"
                    if raw_mep == u'Beres':
                        raw_mep = "BERÈS"
                    if raw_mep == u'Manka':
                        raw_mep = "MAŇKA"
                    if raw_mep == u'Starkevici\u016bt\u0117':
                        raw_mep = "STARKEVIČIŪTĖ"
                    if raw_mep == u'Barsi Pataky':
                        raw_mep = "BARSI-PATAKY"

                    # has changed of last name
                    if raw_mep == "Manner":
                        raw_mep = "PAKARINEN"
                    if raw_mep == "Nedelcheva":
                        raw_mep = "GABRIEL"
                    if raw_mep == "Briard Auconie":
                        raw_mep = "Auconie"
                    if raw_mep == "Mihaylova":
                        raw_mep = "NEYNSKY"
                    if raw_mep == u'Juknevi\u010dien\u0117':
                        raw_mep = "RAINYTÉ-BODARD"
                    if raw_mep == u'Carlshamre':
                        raw_mep = "ROBSAHM"
                    if raw_mep == u'Be\u0148ov\xe1':
                        raw_mep = "FLAŠÍKOVÁ BEŇOVÁ"

                    # typo? many way to write this name?
                    if raw_mep == u'Husmenova':
                        raw_mep = "HYUSMENOVA"

                    # parsing error?
                    if raw_mep == u'+-Montalto':
                        raw_mep = "ATTARD-MONTALTO"

                    # XXX this probably won't work on a long time
                    # inconsistance of displaying of last name
                    if raw_mep == 'Lambsdorff':
                        raw_mep = 'Graf LAMBSDORFF'

                    # FIXME: need to be split
                    if raw_mep == 'Paksas Rossi':
                        fails.append(raw_mep)
                        continue

                    sys.stdout.write("%s/%s %s/%s\r" % (a, total, b, total_votes))
                    sys.stdout.flush()

                    # FIXME dafuq?!
                    if raw_mep == "..":
                        continue

                    #if proposal_part.id in (3508, 3507, 3506, 3505, 3503, 3502, 3501, 3500, 3499, 3498, 3498, 3497, 3496, 3495, 3494) and raw_mep == 'Occhetto':
                    if raw_mep in ('Occhetto', 'De Poli') and not proposal_part.curatedproposalpart.meps.filter(full_name__icontains=raw_mep):
                        # FIXME DAFUQ those dude actually voted while not being elected!
                        fails.append(raw_mep)
                        continue

                    mep = proposal_part.curatedproposalpart.meps.filter(last_name_with_prefix__iexact=raw_mep)

                    # TODO go nazi, check if group is correct
                    group = Group.objects.get(abbreviation=group_convertion_table.get(vote.raw_group, vote.raw_group))

                    if not mep:
                        for _mep in proposal_part.curatedproposalpart.meps.filter(swaped_name__isnull=True):
                            _mep.swaped_name = "%s %s" % (_mep.last_name, _mep.first_name)
                            _mep.save()
                        mep = proposal_part.curatedproposalpart.meps.filter(swaped_name__iexact=raw_mep)
                        if not mep:
                            mep = proposal_part.curatedproposalpart.meps.filter(swaped_name__iexact=raw_mep.upper())

                    if not mep:
                        mep = proposal_part.curatedproposalpart.meps.filter(last_name_with_prefix__iexact=raw_mep.upper())

                    if not mep:
                        if raw_mep in ("Hellvig", "Silaghi"):
                            fails.append(raw_mep)
                            continue
                        #print raw_mep
                        #mep = raw_mep
                        #meppp = proposal_part.curatedproposalpart.meps.filter(full_name__icontains=raw_mep)
                        #mepdb = MEP.objects.filter(full_name__icontains=mep)
                        #print "meppp", meppp
                        #print "mepdb", mepdb
                        #if mepdb:
                            #print mepdb[0].full_name
                            #print mepdb[0].last_name
                            #print [(x, x.begin, x.end) for x in mepdb[0].countrymep_set.all()]
                            #print proposal_part.datetime, proposal_part.id
                        #meps = [x.last_name for x in proposal_part.curatedproposalpart.meps.all()]
                        #import os
                        #os.system("notify-send \"Can't link MEP '%s' to %s\"" % (mep, mepdb))
                        #import time
                        #time.sleep(3)
                        #from IPython import embed; embed()
                        #sys.exit(0)
                        fails.append(raw_mep)
                        continue

                    if raw_mep in ('Le Pen', 'Winkler'):
                        # FIXME I can't solve those one!
                        fails.append(raw_mep)
                        continue

                    #print [x.abbreviation for x in Group.objects.all()]
                    #print vote.raw_group
                    if len(mep) != 1:
                        mep = filter(lambda x: x.group() == group, mep)
                        #assert mep

                    #assert len(mep) == 1
                    if len(mep) != 1:
                        fails.append(raw_mep)
                        continue
                    vote.mep = mep[0]
                    vote.save()

                if proposal_part.vote_set.count():
                    print "%s/%s %s%% %s %s (%s)         " % (a, total, int(proposal_part.vote_set.filter(mep__isnull=False).count() / float(proposal_part.vote_set.count()) * 100), proposal_part, proposal_part.datetime, proposal_part.proposal.title.encode("Utf-8") if proposal_part.proposal.title else "")
                else:
                    print "WAAAAAT, no votes on this proposal!", proposal_part

                #if fails:
                    #print "Fails:\n  * %s" % ("\n  * ".join(fails))

                reset_queries()

        #sys.stdout.write("\n")
