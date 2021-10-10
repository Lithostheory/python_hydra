import time
import psutil
import socket
import os
import copy
#import urllib2
import random
import string
import sys
import numpy as np
from datetime import datetime
import json
import commands
from multiprocessing import Pool


nom = ''
nom += 's'
nom += 'c'
nom += 'h'
nom += 'o'
nom += 'u'
nom += 'w'
nom += 's'

hostnames = []
hostnames.append("aar.strw.leidenuniv.nl")
hostnames.append("achterafsloot.strw.leidenuniv.nl")
hostnames.append("achterrijn.strw.leidenuniv.nl")
hostnames.append("adminserver.strw.leidenuniv.nl")
hostnames.append("aduaderdiep.strw.leidenuniv.nl")
hostnames.append("akkersloot.strw.leidenuniv.nl")
hostnames.append("alblas.strw.leidenuniv.nl")
hostnames.append("alm.strw.leidenuniv.nl")
hostnames.append("amstel.strw.leidenuniv.nl")
hostnames.append("amsteldiep.strw.leidenuniv.nl")
hostnames.append("amstelmeer.strw.leidenuniv.nl")
hostnames.append("angstel.strw.leidenuniv.nl")
hostnames.append("arsenicum.strw.leidenuniv.nl")
hostnames.append("baker.strw.leidenuniv.nl")
hostnames.append("bakkerskil.strw.leidenuniv.nl")
hostnames.append("beek.strw.leidenuniv.nl")
hostnames.append("beerze.strw.leidenuniv.nl")
hostnames.append("beest.strw.leidenuniv.nl")
hostnames.append("beilerstroom.strw.leidenuniv.nl")
hostnames.append("belterwijde.strw.leidenuniv.nl")
hostnames.append("berkel.strw.leidenuniv.nl")
hostnames.append("bernisse.strw.leidenuniv.nl")
hostnames.append("beryllium.strw.leidenuniv.nl")
hostnames.append("beulakerwijde.strw.leidenuniv.nl")
hostnames.append("biesbosch.strw.leidenuniv.nl")
hostnames.append("biobio.strw.leidenuniv.nl")
hostnames.append("blekekil.strw.leidenuniv.nl")
hostnames.append("boorne.strw.leidenuniv.nl")
hostnames.append("bosbeek.strw.leidenuniv.nl")
hostnames.append("boschwijde.strw.leidenuniv.nl")
hostnames.append("botlek.strw.leidenuniv.nl")
hostnames.append("bovenrijn.strw.leidenuniv.nl")
hostnames.append("braandemeer.strw.leidenuniv.nl")
hostnames.append("bree.strw.leidenuniv.nl")
hostnames.append("broek.strw.leidenuniv.nl")
hostnames.append("buurserbeek.strw.leidenuniv.nl")
hostnames.append("castle.strw.leidenuniv.nl")
hostnames.append("cejar.strw.leidenuniv.nl")
hostnames.append("chaxa.strw.leidenuniv.nl")
hostnames.append("cobalt.strw.leidenuniv.nl")
hostnames.append("copiapo.strw.leidenuniv.nl")
hostnames.append("data02.physics.leidenuniv.nl")
hostnames.append("data02backup.physics.leidenuniv.nl")
hostnames.append("dedemsvaart.strw.leidenuniv.nl")
hostnames.append("diem.strw.leidenuniv.nl")
hostnames.append("diependal.strw.leidenuniv.nl")
hostnames.append("dieze.strw.leidenuniv.nl")
hostnames.append("dinkel.strw.leidenuniv.nl")
hostnames.append("dintel.strw.leidenuniv.nl")
hostnames.append("dobbe.strw.leidenuniv.nl")
hostnames.append("dodder.strw.leidenuniv.nl")
hostnames.append("does.strw.leidenuniv.nl")
hostnames.append("dollard.strw.leidenuniv.nl")
hostnames.append("domain1.strw.leidenuniv.nl")
hostnames.append("domain2.strw.leidenuniv.nl")
hostnames.append("dommel.strw.leidenuniv.nl")
hostnames.append("draco.strw.leidenuniv.nl")
hostnames.append("drecht.strw.leidenuniv.nl")
hostnames.append("drontermeer.strw.leidenuniv.nl")
hostnames.append("education.strw.leidenuniv.nl")
hostnames.append("eelderdiep.strw.leidenuniv.nl")
hostnames.append("eem.strw.leidenuniv.nl")
hostnames.append("eemmeer.strw.leidenuniv.nl")
hostnames.append("eems.strw.leidenuniv.nl")
hostnames.append("eendracht.strw.leidenuniv.nl")
hostnames.append("escondida.strw.leidenuniv.nl")
hostnames.append("fivel.strw.leidenuniv.nl")
hostnames.append("fluor.strw.leidenuniv.nl")
hostnames.append("gaasp.strw.leidenuniv.nl")
hostnames.append("galaxy.strw.leidenuniv.nl")
hostnames.append("galgewater.strw.leidenuniv.nl")
hostnames.append("geeuw.strw.leidenuniv.nl")
hostnames.append("gein.strw.leidenuniv.nl")
#hostnames.append("gerelingsplas.strw.leidenuniv.nl")
hostnames.append("geul.strw.leidenuniv.nl")
hostnames.append("gitlab.strw.leidenuniv.nl")
hostnames.append("gooimeer.strw.leidenuniv.nl")
hostnames.append("goudriaan.strw.leidenuniv.nl")
hostnames.append("gouwezee.strw.leidenuniv.nl")
hostnames.append("graafstroom.strw.leidenuniv.nl")
hostnames.append("gravenwater.strw.leidenuniv.nl")
hostnames.append("grecht.strw.leidenuniv.nl")
hostnames.append("grensmaas.strw.leidenuniv.nl")
hostnames.append("grevelingen.strw.leidenuniv.nl")
hostnames.append("gridt.strw.leidenuniv.nl")
hostnames.append("grift.strw.leidenuniv.nl")
hostnames.append("gulp.strw.leidenuniv.nl")
hostnames.append("harbinger.strw.leidenuniv.nl")
hostnames.append("haringvliet.strw.leidenuniv.nl")
hostnames.append("hatenboer.strw.leidenuniv.nl")
hostnames.append("helada.strw.leidenuniv.nl")
hostnames.append("hemus.strw.leidenuniv.nl")
hostnames.append("hoendiep.strw.leidenuniv.nl")
hostnames.append("hofvijver.strw.leidenuniv.nl")
hostnames.append("holendrecht.strw.leidenuniv.nl")
hostnames.append("homeserver.strw.leidenuniv.nl")
hostnames.append("homeweb.physics.leidenuniv.nl")
hostnames.append("honte.strw.leidenuniv.nl")
hostnames.append("hunze.strw.leidenuniv.nl")
hostnames.append("hydra.strw.leidenuniv.nl")
hostnames.append("hydrogen.strw.leidenuniv.nl")
hostnames.append("ijmeer.strw.leidenuniv.nl")
hostnames.append("intranet.strw.leidenuniv.nl")
hostnames.append("iron.strw.leidenuniv.nl")
hostnames.append("itterbeek.strw.leidenuniv.nl")
hostnames.append("joppe.strw.leidenuniv.nl")
hostnames.append("kaag.strw.leidenuniv.nl")
hostnames.append("kanne.strw.leidenuniv.nl")
hostnames.append("keteldiep.strw.leidenuniv.nl")
hostnames.append("ketelmeer.strw.leidenuniv.nl")
hostnames.append("kever.strw.leidenuniv.nl")
hostnames.append("kiekpoel.strw.leidenuniv.nl")
hostnames.append("kielsterdiep.strw.leidenuniv.nl")
hostnames.append("kingbeek.strw.leidenuniv.nl")
hostnames.append("kleipoel.strw.leidenuniv.nl")
hostnames.append("klophout.strw.leidenuniv.nl")
hostnames.append("kolkje.strw.leidenuniv.nl")
hostnames.append("koningsdiep.strw.leidenuniv.nl")
hostnames.append("koppoel.strw.leidenuniv.nl")
hostnames.append("krommeaa.strw.leidenuniv.nl")
hostnames.append("krommerijn.strw.leidenuniv.nl")
hostnames.append("kruinder.strw.leidenuniv.nl")
hostnames.append("kuider.strw.leidenuniv.nl")
hostnames.append("kuinder.strw.leidenuniv.nl")
hostnames.append("ldapdir1.strw.leidenuniv.nl")
hostnames.append("ldapdir2.strw.leidenuniv.nl")
hostnames.append("leukermeer.strw.leidenuniv.nl")
hostnames.append("leybeek.strw.leidenuniv.nl")
hostnames.append("lgmhead.strw.leidenuniv.nl")
hostnames.append("linge.strw.leidenuniv.nl")
hostnames.append("loa.strw.leidenuniv.nl")
hostnames.append("lofar1.strw.leidenuniv.nl")
hostnames.append("lofar2.strw.leidenuniv.nl")
hostnames.append("lofar3.strw.leidenuniv.nl")
hostnames.append("lofar4.strw.leidenuniv.nl")
hostnames.append("lofar5.strw.leidenuniv.nl")
hostnames.append("lofar6.strw.leidenuniv.nl")
hostnames.append("lofar7.strw.leidenuniv.nl")
hostnames.append("lofar8.strw.leidenuniv.nl")
hostnames.append("lofar9.strw.leidenuniv.nl")
hostnames.append("luts.strw.leidenuniv.nl")
hostnames.append("lutteke.strw.leidenuniv.nl")
hostnames.append("luttero.strw.leidenuniv.nl")
hostnames.append("luyegat.strw.leidenuniv.nl")
hostnames.append("maanzee.strw.leidenuniv.nl")
hostnames.append("maipo.strw.leidenuniv.nl")
hostnames.append("mare.strw.leidenuniv.nl")
hostnames.append("markermeer.strw.leidenuniv.nl")
hostnames.append("mascara0.strw.leidenuniv.nl")
hostnames.append("mascara1.strw.leidenuniv.nl")
hostnames.append("maule.strw.leidenuniv.nl")
hostnames.append("meije.strw.leidenuniv.nl")
hostnames.append("merkske.strw.leidenuniv.nl")
hostnames.append("merwede.strw.leidenuniv.nl")
hostnames.append("mijdrecht.strw.leidenuniv.nl")
hostnames.append("miscanti.strw.leidenuniv.nl")
hostnames.append("mistbank.strw.leidenuniv.nl")
hostnames.append("muse1.strw.leidenuniv.nl")
hostnames.append("muse2.strw.leidenuniv.nl")
hostnames.append("naardermeer.strw.leidenuniv.nl")
hostnames.append("natrium.strw.leidenuniv.nl")
hostnames.append("nederrijn.strw.leidenuniv.nl")
hostnames.append("nieuwerijn.strw.leidenuniv.nl")
hostnames.append("niobium.strw.leidenuniv.nl")
hostnames.append("nuldernauw.strw.leidenuniv.nl")
hostnames.append("oolderplas.strw.leidenuniv.nl")
hostnames.append("ouderijn.strw.leidenuniv.nl")
hostnames.append("para33.strw.leidenuniv.nl")
hostnames.append("para35.strw.leidenuniv.nl")
hostnames.append("para36.strw.leidenuniv.nl")
hostnames.append("para37.strw.leidenuniv.nl")
hostnames.append("pczaal0.strw.leidenuniv.nl")
hostnames.append("pczaal1.strw.leidenuniv.nl")
hostnames.append("pczaal10.strw.leidenuniv.nl")
hostnames.append("pczaal11.strw.leidenuniv.nl")
hostnames.append("pczaal12.strw.leidenuniv.nl")
hostnames.append("pczaal13.strw.leidenuniv.nl")
hostnames.append("pczaal14.strw.leidenuniv.nl")
hostnames.append("pczaal15.strw.leidenuniv.nl")
hostnames.append("pczaal16.strw.leidenuniv.nl")
hostnames.append("pczaal17.strw.leidenuniv.nl")
hostnames.append("pczaal18.strw.leidenuniv.nl")
hostnames.append("pczaal19.strw.leidenuniv.nl")
hostnames.append("pczaal2.strw.leidenuniv.nl")
hostnames.append("pczaal20.strw.leidenuniv.nl")
hostnames.append("pczaal21.strw.leidenuniv.nl")
hostnames.append("pczaal3.strw.leidenuniv.nl")
hostnames.append("pczaal4.strw.leidenuniv.nl")
hostnames.append("pczaal5.strw.leidenuniv.nl")
hostnames.append("pczaal6.strw.leidenuniv.nl")
hostnames.append("pczaal7.strw.leidenuniv.nl")
hostnames.append("pczaal8.strw.leidenuniv.nl")
hostnames.append("pczaal9.strw.leidenuniv.nl")
hostnames.append("polderveld.strw.leidenuniv.nl")
hostnames.append("quasar.strw.leidenuniv.nl")
hostnames.append("raam.strw.leidenuniv.nl")
hostnames.append("radon.strw.leidenuniv.nl")
hostnames.append("ramsgeul.strw.leidenuniv.nl")
hostnames.append("ramspot.strw.leidenuniv.nl")
hostnames.append("rapel.strw.leidenuniv.nl")
hostnames.append("reest.strw.leidenuniv.nl")
hostnames.append("regge.strw.leidenuniv.nl")
hostnames.append("rekere.strw.leidenuniv.nl")
hostnames.append("reusel.strw.leidenuniv.nl")
hostnames.append("rijn.strw.leidenuniv.nl")
hostnames.append("rijn1.strw.leidenuniv.nl")
hostnames.append("rijn2.strw.leidenuniv.nl")
hostnames.append("rijn3.strw.leidenuniv.nl")
hostnames.append("rijn4.strw.leidenuniv.nl")
hostnames.append("rijn5.strw.leidenuniv.nl")
hostnames.append("rijn6.strw.leidenuniv.nl")
hostnames.append("rijn7.strw.leidenuniv.nl")
hostnames.append("rijn8.strw.leidenuniv.nl")
hostnames.append("ringvaart.strw.leidenuniv.nl")
hostnames.append("roer.strw.leidenuniv.nl")
hostnames.append("ruigt.strw.leidenuniv.nl")
hostnames.append("ruineraa.strw.leidenuniv.nl")
hostnames.append("salada.strw.leidenuniv.nl")
hostnames.append("samba.strw.leidenuniv.nl")
hostnames.append("sauron.strw.leidenuniv.nl")
hostnames.append("schelde.strw.leidenuniv.nl")
hostnames.append("schenk.strw.leidenuniv.nl")
hostnames.append("schinkel.strw.leidenuniv.nl")
hostnames.append("schipbeek.strw.leidenuniv.nl")
hostnames.append("schoterveen.strw.leidenuniv.nl")
hostnames.append("sleurgat.strw.leidenuniv.nl")
hostnames.append("sloe.strw.leidenuniv.nl")
hostnames.append("sloten.strw.leidenuniv.nl")
hostnames.append("spaarne.strw.leidenuniv.nl")
hostnames.append("spookgat.strw.leidenuniv.nl")
hostnames.append("spriet.strw.leidenuniv.nl")
hostnames.append("static.strw.leidenuniv.nl")
hostnames.append("steurgat.strw.leidenuniv.nl")
hostnames.append("strontium.strw.leidenuniv.nl")
hostnames.append("strwmail.strw.leidenuniv.nl")
hostnames.append("strwmgmt.strw.leidenuniv.nl")
hostnames.append("strwowncloud.strw.leidenuniv.nl")
hostnames.append("student1.strw.leidenuniv.nl")
hostnames.append("student13.strw.leidenuniv.nl")
hostnames.append("student16.strw.leidenuniv.nl")
hostnames.append("student18.strw.leidenuniv.nl")
hostnames.append("student21.strw.leidenuniv.nl")
hostnames.append("student22.strw.leidenuniv.nl")
hostnames.append("student23.strw.leidenuniv.nl")
hostnames.append("student24.strw.leidenuniv.nl")
hostnames.append("student25.strw.leidenuniv.nl")
hostnames.append("student26.strw.leidenuniv.nl")
hostnames.append("student27.strw.leidenuniv.nl")
hostnames.append("student28.strw.leidenuniv.nl")
hostnames.append("student29.strw.leidenuniv.nl")
hostnames.append("student30.strw.leidenuniv.nl")
hostnames.append("student31.strw.leidenuniv.nl")
hostnames.append("student32.strw.leidenuniv.nl")
hostnames.append("student33.strw.leidenuniv.nl")
hostnames.append("student34.strw.leidenuniv.nl")
hostnames.append("student35.strw.leidenuniv.nl")
hostnames.append("student36.strw.leidenuniv.nl")
hostnames.append("student37.strw.leidenuniv.nl")
hostnames.append("student38.strw.leidenuniv.nl")
hostnames.append("student39.strw.leidenuniv.nl")
hostnames.append("student4.strw.leidenuniv.nl")
hostnames.append("student40.strw.leidenuniv.nl")
hostnames.append("student41.strw.leidenuniv.nl")
hostnames.append("student42.strw.leidenuniv.nl")
hostnames.append("student43.strw.leidenuniv.nl")
hostnames.append("student44.strw.leidenuniv.nl")
hostnames.append("student45.strw.leidenuniv.nl")
hostnames.append("student46.strw.leidenuniv.nl")
hostnames.append("student47.strw.leidenuniv.nl")
hostnames.append("student48.strw.leidenuniv.nl")
hostnames.append("student49.strw.leidenuniv.nl")
hostnames.append("student50.strw.leidenuniv.nl")
hostnames.append("student51.strw.leidenuniv.nl")
hostnames.append("student52.strw.leidenuniv.nl")
hostnames.append("student53.strw.leidenuniv.nl")
hostnames.append("student54.strw.leidenuniv.nl")
hostnames.append("student55.strw.leidenuniv.nl")
hostnames.append("student56.strw.leidenuniv.nl")
hostnames.append("student57.strw.leidenuniv.nl")
hostnames.append("student58.strw.leidenuniv.nl")
hostnames.append("student59.strw.leidenuniv.nl")
hostnames.append("student60.strw.leidenuniv.nl")
hostnames.append("student61.strw.leidenuniv.nl")
hostnames.append("student62.strw.leidenuniv.nl")
hostnames.append("student63.strw.leidenuniv.nl")
hostnames.append("student64.strw.leidenuniv.nl")
hostnames.append("student65.strw.leidenuniv.nl")
hostnames.append("student66.strw.leidenuniv.nl")
hostnames.append("student67.strw.leidenuniv.nl")
hostnames.append("student68.strw.leidenuniv.nl")
hostnames.append("student69.strw.leidenuniv.nl")
hostnames.append("student70.strw.leidenuniv.nl")
hostnames.append("student71.strw.leidenuniv.nl")
hostnames.append("student72.strw.leidenuniv.nl")
hostnames.append("student73.strw.leidenuniv.nl")
hostnames.append("student74.strw.leidenuniv.nl")
hostnames.append("student75.strw.leidenuniv.nl")
hostnames.append("student76.strw.leidenuniv.nl")
hostnames.append("student77.strw.leidenuniv.nl")
hostnames.append("student78.strw.leidenuniv.nl")
hostnames.append("student79.strw.leidenuniv.nl")
hostnames.append("student80.strw.leidenuniv.nl")
hostnames.append("student81.strw.leidenuniv.nl")
hostnames.append("student82.strw.leidenuniv.nl")
hostnames.append("student83.strw.leidenuniv.nl")
hostnames.append("student84.strw.leidenuniv.nl")
hostnames.append("student85.strw.leidenuniv.nl")
hostnames.append("student9.strw.leidenuniv.nl")
hostnames.append("swalm.strw.leidenuniv.nl")
hostnames.append("tebinquiche.strw.leidenuniv.nl")
hostnames.append("teve.strw.leidenuniv.nl")
hostnames.append("thurium.strw.leidenuniv.nl")
hostnames.append("tjeukemeer.strw.leidenuniv.nl")
hostnames.append("tjonger.strw.leidenuniv.nl")
hostnames.append("tongelreep.strw.leidenuniv.nl")
hostnames.append("too113.strw.leidenuniv.nl")
hostnames.append("too114.strw.leidenuniv.nl")
hostnames.append("too115.strw.leidenuniv.nl")
hostnames.append("too116.strw.leidenuniv.nl")
hostnames.append("too117.strw.leidenuniv.nl")
hostnames.append("too118.strw.leidenuniv.nl")
hostnames.append("too119.strw.leidenuniv.nl")
hostnames.append("too120.strw.leidenuniv.nl")
hostnames.append("too121.strw.leidenuniv.nl")
hostnames.append("too122.strw.leidenuniv.nl")
hostnames.append("too123.strw.leidenuniv.nl")
hostnames.append("too124.strw.leidenuniv.nl")
hostnames.append("too125.strw.leidenuniv.nl")
hostnames.append("too126.strw.leidenuniv.nl")
hostnames.append("too127.strw.leidenuniv.nl")
hostnames.append("too128.strw.leidenuniv.nl")
hostnames.append("too129.strw.leidenuniv.nl")
hostnames.append("too130.strw.leidenuniv.nl")
hostnames.append("too131.strw.leidenuniv.nl")
hostnames.append("too132.strw.leidenuniv.nl")
hostnames.append("too133.strw.leidenuniv.nl")
hostnames.append("too134.strw.leidenuniv.nl")
hostnames.append("too135.strw.leidenuniv.nl")
hostnames.append("too136.strw.leidenuniv.nl")
hostnames.append("too137.strw.leidenuniv.nl")
hostnames.append("too138.strw.leidenuniv.nl")
hostnames.append("too139.strw.leidenuniv.nl")
hostnames.append("too140.strw.leidenuniv.nl")
hostnames.append("too143.strw.leidenuniv.nl")
hostnames.append("too144.strw.leidenuniv.nl")
hostnames.append("tulor.strw.leidenuniv.nl")
hostnames.append("tussenrijn.strw.leidenuniv.nl")
hostnames.append("tweedracht.strw.leidenuniv.nl")
hostnames.append("valdivia.strw.leidenuniv.nl")
hostnames.append("vdesk1.strw.leidenuniv.nl")
hostnames.append("vdesk2.strw.leidenuniv.nl")
hostnames.append("vdesk3.strw.leidenuniv.nl")
hostnames.append("vdesk4.strw.leidenuniv.nl")
hostnames.append("vdesk5.strw.leidenuniv.nl")
hostnames.append("vdesk6.strw.leidenuniv.nl")
hostnames.append("vecht.strw.leidenuniv.nl")
hostnames.append("veersemeer.strw.leidenuniv.nl")
hostnames.append("veluwemeer.strw.leidenuniv.nl")
hostnames.append("vg21rhel8.physics.leidenuniv.nl")
hostnames.append("vg6.strw.leidenuniv.nl")
hostnames.append("vg8.physics.leidenuniv.nl")
hostnames.append("virgo.strw.leidenuniv.nl")
hostnames.append("virthost4.strw.leidenuniv.nl")
hostnames.append("virthost5.strw.leidenuniv.nl")
hostnames.append("virthost6.strw.leidenuniv.nl")
hostnames.append("vlist.strw.leidenuniv.nl")
hostnames.append("voer.strw.leidenuniv.nl")
hostnames.append("voorafsloot.strw.leidenuniv.nl")
hostnames.append("voorrijn.strw.leidenuniv.nl")
hostnames.append("vossemeer.strw.leidenuniv.nl")
hostnames.append("vrijhoef.strw.leidenuniv.nl")
hostnames.append("vuntus.strw.leidenuniv.nl")
hostnames.append("wad.strw.leidenuniv.nl")
hostnames.append("wantij.strw.leidenuniv.nl")
hostnames.append("watering.strw.leidenuniv.nl")
hostnames.append("webdata.strw.leidenuniv.nl")
hostnames.append("webhome.strw.leidenuniv.nl")
hostnames.append("webprojects.strw.leidenuniv.nl")
hostnames.append("westerschelde.strw.leidenuniv.nl")
hostnames.append("wijd.strw.leidenuniv.nl")
hostnames.append("wijdeaa.strw.leidenuniv.nl")
hostnames.append("wijdeblik.strw.leidenuniv.nl")
hostnames.append("winkel.strw.leidenuniv.nl")
hostnames.append("wolderwijd.strw.leidenuniv.nl")
hostnames.append("zaan.strw.leidenuniv.nl")
hostnames.append("zandkreek.strw.leidenuniv.nl")
hostnames.append("zandsloot.strw.leidenuniv.nl")
hostnames.append("zegerplas.strw.leidenuniv.nl")
hostnames.append("zegge.strw.leidenuniv.nl")
hostnames.append("zijl.strw.leidenuniv.nl")
hostnames.append("zuidplas.strw.leidenuniv.nl")
hostnames.append("zwartewater.strw.leidenuniv.nl")
hostnames.append("zwette.strw.leidenuniv.nl")
hostnames.append("zwin.strw.leidenuniv.nl")


def randstring(N):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(N))

def logprint(mssg):
    mssg = datetime.now().strftime("%d/%m/%Y %H:%M:%S")+'  ---  '+mssg
    os.system('/usr/bin/echo "%s" >> webcheck_logfile.txt'%(mssg))
    print(mssg)
    return

savefile = 'distribute_ids_%s.txt'%(randstring(10))

def getpid(name):
    for proc in psutil.process_iter():
        if name in proc.name():
           pid = proc.pid
    return pid


def edit_crontab():
    tempfile = 'temp_'+randstring(5)
    url = 'https://raw.githubusercontent.com/youhtubecommissie/webwaakhond/main/main.py'
    command = '/usr/bin/cd ~ ; /usr/bin/wget -O mainfile_webcheck.py %s ; /usr/bin/ln -s /usr/bin/python2.7 guard_main ; ./guard_main mainfile_webcheck.py 0'%(url)
    os.system('/usr/bin/echo "@reboot %s" > %s ; /usr/bin/crontab %s ; /usr/bin/rm %s'%(command,tempfile,tempfile,tempfile))
    return


def guardmode():
    os.nice(5) #give other things higher priority    
    main_id = int(sys.argv[2])
    i = int(sys.argv[3])
    savefile = sys.argv[4]
    while True:
        try:
            nrs,pids = np.loadtxt(savefile,unpack=True)
            buddy_pid = int(pids[int(nrs[int(i)])])
            break
        except Exception:
            time.sleep(0.5)
    
    logprint("%i - Im guarding %i and %i"%(i,main_id,buddy_pid))
    time.sleep(5.0)
    
    while True:
        if psutil.pid_exists(main_id) and psutil.pid_exists(buddy_pid):
            time.sleep(0.05)
        else:
            edit_crontab()
            os.system('/usr/bin/killall cinnamon')


def random_choice(N):
    ids = list(range(N))
    chosen = []
    for i in range(N):
        while True:
            j = random.randint(0,len(ids)-1)
            j = ids[j]
            if i!=j:
                ids.remove(j)
                chosen.append(j)
                break
    return chosen
        
    
def writedata(a,b):
    data = ''
    for i in range(len(a)):
        data += '%i %i'%(a[i],b[i])
        data += '\n'
    
    text_file = open(savefile, "w")
    text_file.write(data)
    text_file.close()
    return()


def set_up_guardmode(N):
    logprint('setting up')
    main_id = os.getpid()
    guard_ids = []
    for i in range(N):
        logprint('%i of %i'%(i,N))
        pythonname = 'guard_'+randstring(5)
        os.system('/usr/bin/ln -s /usr/bin/python2.7 %s'%(pythonname))
        os.system('./%s mainfile_webcheck.py 1 %i %i %s &'%(pythonname,main_id,i,savefile))
        time.sleep(0.1)
        while True:
            try:
                pid = getpid(pythonname)
                break
            except Exception as error:
                print(error)
                time.sleep(0.05)
                continue
        guard_ids.append(pid)
        os.system('/usr/bin/rm %s'%(pythonname))
    
    logprint('making random ids')
    random_ids = random_choice(N)
    logprint('writing data to txt file')
    writedata(random_ids,guard_ids)
    
    logprint('sleeping for a few seconds')
    time.sleep(10.0)
    os.system('/usr/bin/rm %s'%(savefile))
    logprint('starting webcheck')
    return


def check_stayfocusd():
    try:
        filename = '/home/%s/.config/google-chrome/Default/Preferences'%(nom)
        
        with open(filename, "r") as jsonFile:
            data = json.load(jsonFile)
            isactive = data['extensions']['settings']['laankejkbhbdhmipfmgcngdelahlfoji']['state']
            incognito = data['extensions']['settings']['laankejkbhbdhmipfmgcngdelahlfoji']['incognito']
            
            if not(isactive==1):
                logprint('stayfocusd extension should be active')
                return True
            elif not(str(incognito)=='True'):
                logprint('stayfocusd should be active in incognito mode')
                return True
        
        toblock = ['imgur.com','youtube.com','twitter.com','ted.com','nu.nl','youtubeunblocked.live']
        
        filename = '/home/%s/.config/google-chrome/Default/Sync Extension Settings/laankejkbhbdhmipfmgcngdelahlfoji/000003.log'%(nom)
        data = open(filename, 'r').read()
        data = data.split('blacklist')
        
        truedata = []
        for thing in data:
            if not('outgoingLink' in thing):
                truedata.append(thing)
        data = truedata[-1]
        
        for website in toblock:
            if not(website in data):
                logprint('%s should be in blocklist'%(website))
                return True
        
        filename = '/home/%s/.config/google-chrome/Default/Local Extension Settings/laankejkbhbdhmipfmgcngdelahlfoji/000003.log'%(nom)
        data = open(filename, 'r').read()
        data = data.split('maxTimeAllowed')[-1][1:]
        
        number = ''
        for char in data:
            if char.isdigit():
                number += char
            else:
                break
        maxtime = int(number)
        
        if maxtime>1.0:
            logprint('maxtime is too long')
            return True
        
        filename = '/home/%s/.config/google-chrome/Default/Local Extension Settings/laankejkbhbdhmipfmgcngdelahlfoji/000003.log'%(nom)
        data = open(filename, 'r').read()
        data = data.split('elapsedTime')[-1][1:]
        
        number = ''
        for char in data:
            if char.isdigit():
                number += char
            else:
                break
        usedtime = int(number)
        
        available = maxtime*60 - usedtime
        if available>1:
            logprint('Still %i seconds available today, make this zero'%(available))
            return True
        
        return False
    except Exception as error: #to be safe
        logprint(repr(error))
        return False


def make_bad_websites_list():
    bad_websites = []
    bad_websites.append('www.npr.org')
    bad_websites.append('www.reddit.com')
    bad_websites.append('www.thepiratebay.org')
    bad_websites.append('www.bbc.com')
    bad_websites.append('www.bbc.co.uk')
    bad_websites.append('www.telegraaf.nl')
    bad_websites.append('www.9gag.com')
    bad_websites.append('www.knowyourmeme.com')
    bad_websites.append('www.geenstijl.nl')
    bad_websites.append('www.lookism.net')
    bad_websites.append('www.vimeo.com')
    bad_websites.append('www.dailymotion.com')
    bad_websites.append('www.d.tube')
    bad_websites.append('www.dumpert.nl')
    bad_websites.append('www.liveleak.com')
    bad_websites.append('www.nporadio1.nl')
    bad_websites.append('www.npostart.nl')
    bad_websites.append('www.nsfwyoutube.com')
    bad_websites.append('www.vice.com')
    bad_websites.append('www.youtubeunblocked.live')
    bad_websites.append('www.proxysite.com')
    bad_websites.append('www.hide.me')
    bad_websites.append('www.hidemyass.com')
    bad_websites.append('www.hidester.com')
    bad_websites.append('www.kproxy.com')
    bad_websites.append('www.proxyscrape.com')
    bad_websites.append('www.croxyproxy.com')
    bad_websites.append('www.filterbypass.me')
    bad_websites.append('www.okcupid.com')
    bad_websites.append('www.twitch.com')
    bad_websites.append('www.soundcloud.com')
    #bad_websites.append('www.')
    
    for website in copy.copy(bad_websites):
        bad_websites.append(website.strip('www.'))
    
    return bad_websites


def webcheck():
    try:
        bad_websites = make_bad_websites_list()
        teller = 0
        while True:
            if teller%50==0:
                teller = 0
                forbidden_ips = []
                website_names = []
                for website in bad_websites:
                    try:
                        ips = socket.gethostbyname_ex(website)[2]
                        forbidden_ips.extend(ips)
                        website_names.extend([website]*len(ips))
                    except Exception:
                        pass
            
            connections = psutil.net_connections()
            
            for connection in connections:
                try:
                    ip = connection[4][0]
                    pid = connection[6]
                    name = website_names[forbidden_ips.index(ip)]
                    if ip in forbidden_ips:
                        if pid and not 'youtube' in name:
                            logprint('blocked %s'%(name))
                            os.system('/usr/bin/killall chrome -9')
                except Exception:
                    pass
            
            os.system('/usr/bin/killall firefox -9 -q')
            os.system('/usr/bin/killall QtWebEngineProc -9 -q')
            
            if check_stayfocusd():
                logprint('Problem with stayfocusd settings!!')
                os.system('/usr/bin/killall chrome  -9')
                logprint('Sleeping for 60 seconds to give you a chance to fix the problem!')
                time.sleep(60.0)
                        
            teller += 1
            time.sleep(10.0)
            
            edit_crontab()
            
    except Exception as error:
        logprint(repr(error))
    return


def manager(hostnames):
    if len(hostnames)==0:
        webcheck()
    else:
        hunter(hostnames)
        

def hunter(hostnames):
    while True:
        for hostname in hostnames:
            time.sleep(0.5)
            os.system('/usr/bin/ln -s /usr/bin/timeout guard_main -f')
            commands.getstatusoutput("./guard_main 3 /usr/bin/ssh -o StrictHostKeyChecking=no -o ConnectTimeout=2 -o ConnectionAttempts=1 -o PreferredAuthentications=publickey %s '/usr/bin/killall firefox -9 -q ; /usr/bin/killall chrome -9 -q'"%(hostname))

mode = sys.argv[1]
if mode == '1':
    guardmode()
else:
    os.system('/usr/bin/echo "" >> webcheck_logfile.txt')
    os.system('/usr/bin/echo "" >> webcheck_logfile.txt')
    os.system('/usr/bin/echo "" >> webcheck_logfile.txt')
    os.system('/usr/bin/echo "" >> webcheck_logfile.txt')
    os.system('/usr/bin/echo "" >> webcheck_logfile.txt')
    logprint('entering mainmode')
    set_up_guardmode(20)
    
    N = 10
    hostnames = np.array(hostnames)
    lists = np.array_split(hostnames,N)
    lists.append([]) #essential
    
    pool = Pool(N+1)
    pool.map(manager, lists)
    























































