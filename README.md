# Beauveria bassiana evidence extraction (abstract-only)

## Study selection (Phase 2)

| Item | n |
|---|---:|
| Includes (accepted) | 254 |
| 00-key-papers (primary) | 5 |
| 01-existing-products (primary) | 89 |
| 02b_strains_traits (primary) | 7 |
| 02c_formulation_delivery (primary) | 62 |
| 03-autodissemination-social (primary) | 56 |
| 04-nontarget-ecotox (primary) | 31 |
| 05-regulatory-policy (primary) | 4 |
| 06-background-proxies (primary) | 0 |
| Rows co-tagged `02a_efficacy` in `screening_categories_all` | 75 |

Supplemental extract libraries (prior velutina project triage; not all rows are Phase 2 includes):

| Lane | PDFs filed | Extract rows |
|---|---:|---:|
| 00-key-papers (Beauveria + Vespidae) | 8 | 11 |
| 07-vespideae-biocontrol (non-Bb microbes + chemical bait/trap) | 17 | 18 |

## 1 existing-products

### Commercial

| Strain | Notes | Example studies |
|---|---|---|
| GHA | BotaniGard, Mycotrol, BoteGHA; also Aprehend / Xpectro / Xpulse in some abstracts | [Weeks2016](https://doi.org/10.1111/mve.12201); [Machtinger2016](https://doi.org/10.1093/jisesa/iew032) |
| ATCC 74040 | Naturalis / Naturalis-L (sometimes labeled strain NATURALIS) | [Saenz-de-CabezonIrigaray2003](https://doi.org/10.1016/s1049-9644(02)00123-8); [Al-Zurfi2019](http://europepmc.org/theses/ETH/820217) |
| ANT-03 | BioCeres | [Chavez2023](https://doi.org/10.3390/insects14090726); [Nadeau2020](http://europepmc.org/abstract/PMC/PMC7702525) |
| PPRI 5339 | BroadBand and Velifer ES (separate abstracts) | [Goble2011](https://doi.org/10.1080/09583157.2011.608907); [Erler2015](https://doi.org/10.1093/jisesa/iev029) |

### Experimental

| Strain | Notes | Example studies |
|---|---|---|
| AP0101 | Wild strain (Achaia, Greece); compared with GHA and PPRI 5339 | [Mantzoukas2022](https://doi.org/10.3390/microorganisms10112306) |
| GxABT-1 | New endemic isolate; compared with GHA (BotaniGard) | [Dessauvages2024](https://doi.org/10.3390/insects15090697) |
| AL1 | Newly selected strain; Naturalis as comparator | [Oreste2016](https://doi.org/10.1016/j.biocontrol.2016.05.011) |
| ARSEF 2879 | Research collection isolate; Mycotrol GHA as comparator | [Yeo2000](http://europepmc.org/theses/ETH/523877) |
| ARSEF 7152 | Research isolate vs commercial GHA | [Liu2006](https://doi.org/10.1603/0022-0493-99.4.1096) |
| ARSEF 7234 | Research isolate vs commercial GHA | [Liu2006](https://doi.org/10.1603/0022-0493-99.4.1096) |
| ARSEF 7404 | Natural isolate vs BotaniGard | [Meyers2013](https://doi.org/10.1016/j.biocontrol.2013.02.001) |
| Bb-18 | Research strain tested with Botanigard | [Cruz-Cruz2020](http://europepmc.org/abstract/AGR/IND607115348) |
| Bb25 | Iraqi isolate; compared with Mycotrol GHA | [Mohammed2019](http://europepmc.org/abstract/AGR/IND606486035) |
| CHG20 | Mycotrol | [Mohammed2019](http://europepmc.org/abstract/AGR/IND606486035) |
| EA2 | Broadband | [Dlamini2020](http://europepmc.org/abstract/AGR/IND606976509) |
| ECS1/BRIP | Velifer | [Khun2020](https://doi.org/10.1016/j.jip.2020.107437) |
| La90 | Mycotrol | [Mohammed2019](http://europepmc.org/abstract/AGR/IND606486035) |
| Ma42 | Mycotrol | [Mohammed2019](http://europepmc.org/abstract/AGR/IND606486035) |
| P10 | Mycotrol | [Mohammed2019](http://europepmc.org/abstract/AGR/IND606486035) |
| SC4 | Tested alongside Bb Naturalis; not labeled commercial | [VanVlaenderen2025](http://europepmc.org/abstract/AGR/IND609406866) |

### Other codes in cat01 abstracts (non-Bb comparator or unclear)

| Code | Notes | Example studies |
|---|---|---|
| BIPESCO5 | NATURALIS | [Jaber2018](https://doi.org/10.1016/j.biocontrol.2017.11.009); [Jaber2018](https://doi.org/10.1016/j.biocontrol.2018.08.007) |
| F52 | BroadBand, Met52, Mycotrol | [Sullivan2020](https://doi.org/10.1007/s10493-020-00547-6); [Erler2015](https://doi.org/10.1093/jisesa/iev029) |
| KRL-AG2 | Naturalis | [Castrillo2013](https://doi.org/10.1016/j.biocontrol.2013.07.015) |

## 2 efficacy-mechanics-delivery

### Bb targets relative to *Vespa velutina*

Phylogenetic distance among arthropods named in Phase 2 Bb extracts relative to *V. velutina*. Top of Hymenoptera = closest shared ancestry with *V. velutina*. Species lists: all named insects and Acari found in Phase 2 extract/include titles and host fields (n = 120).

```
Arthropoda
├── Acari (mites and ticks)
└── Insecta
    ├── Orthoptera (locusts, grasshoppers)
    ├── Blattodea (termites)
    ├── Thysanoptera (thrips)
    ├── Hemiptera (true bugs, whiteflies, aphids, bed bugs)
    └── Holometabola
        ├── Hymenoptera
        │   ├── Vespa (V. velutina, V. analis)
        │   ├── Other Vespidae (Vespula, Polistes, Mischocyttarus)
        │   ├── Apidae (Apis, Bombus, Meliponula)
        │   ├── Formicidae (ants)
        │   ├── Tenthredinidae (sawflies)
        │   └── Aphelinidae (Encarsia, Eretmocerus)
        ├── Neuroptera (antlions)
        ├── Coleoptera (beetles)
        ├── Lepidoptera (moths)
        └── Diptera (flies, mosquitoes)
```

| Rank | Band | Taxa |
|---:|---|---|
| 1 | Same genus (*Vespa*) | *Vespa velutina*, *Vespa analis* |
| 2 | Same family (Vespidae) | *Vespula germanica*, *Vespula vulgaris*, *Vespula maculifrons*, *Polistes dominula*, *Polistes chinensis*, *Polistes myersi*, *Polistes hebraeus*, *Mischocyttarus metathoracicus* |
| 3 | Apidae | *Apis mellifera*, *Apis cerana*, *Bombus terrestris*, *Bombus impatiens*, *Meliponula ferruginea* |
| 4 | Other Hymenoptera | *Solenopsis invicta*, *Atta cephalotes*, *Camponotus*, *Pristiphora abietina*, *Hoplocampa testudinea*, *Encarsia formosa*, *Eretmocerus eremicus* |
| 5 | Neuroptera | *Myrmeleon timidus* |
| 6 | Coleoptera | *Rhynchophorus ferrugineus*, *Hypothenemus hampei*, *Leptinotarsa decemlineata*, *Agrilus planipennis*, *Monochamus alternatus*, *Enaphalodes rufulus*, *Alphitobius diaperinus*, *Tenebrio molitor*, *Tribolium castaneum*, *Sitophilus oryzae*, *Otiorhynchus sulcatus*, *Hylobius abietis*, *Cosmopolites sordidus*, *Kuschelorhynchus macadamiae*, *Listronotus maculicollis*, *Phlyctinus callosus*, *Blosyrus asellus*, *Carpophilus lugubris*, *Cryptolestes ferrugineus*, *Oryzaephilus surinamensis*, *Rhyzopertha dominica*, *Dendroctonus simplex*, *Dendroctonus ponderosae*, *Ips typographus*, *Ips duplicatus*, *Pityophthorus juglandis*, *Xylosandrus crassiusculus*, *Xylosandrus germanus*, *Euwallacea perbrevis*, *Microtheca ochroloma*, *Dastarcus helophoroides* |
| 7 | Lepidoptera | *Spodoptera frugiperda*, *Dargida diffusa*, *Tuta absoluta*, *Ostrinia nubilalis*, *Galleria mellonella*, *Thaumatotibia leucotreta*, *Cameraria ohridella*, *Plutella xylostella* |
| 8 | Diptera | *Musca domestica*, *Stomoxys calcitrans*, *Lucilia sericata*, *Aedes aegypti*, *Aedes albopictus*, *Aedes notoscriptus*, *Culex quinquefasciatus*, *Ceratitis capitata*, *Anastrepha ludens*, *Bactrocera dorsalis*, *Bactrocera zonata*, *Zeugodacus cucurbitae*, *Rhagoletis cerasi*, *Glossina pallidipes*, *Liriomyza sativae*, *Liriomyza huidobrensis*, *Contarinia nasturtii*, *Sitodiplosis mosellana*, *Lycoriella ingenua*, *Drosophila* |
| 9 | Thysanoptera | *Frankliniella occidentalis*, *Scirtothrips aurantii*, *Scirtothrips dorsalis*, *Thrips parvispinus* |
| 10 | Hemiptera | *Lycorma delicatula*, *Lygus lineolaris*, *Macrolophus pygmaeus*, *Trialeurodes vaporariorum*, *Bemisia tabaci*, *Aleyrodes proletella*, *Cimex lectularius*, *Triatoma infestans*, *Halyomorpha halys*, *Megacopta cribraria*, *Diaphorina citri*, *Myzus persicae*, *Brevicoryne brassicae*, *Nasonovia ribisnigri*, *Rhopalosiphum padi*, *Acanthococcus lagerstroemiae* |
| 11 | Orthoptera | *Schistocerca gregaria*, *Schistocerca americana*, *Melanoplus sanguinipes* |
| 12 | Blattodea | *Odontotermes formosanus*, *Reticulitermes chinensis* |
| 13 | Acari | *Dermanyssus gallinae*, *Psoroptes ovis*, *Ixodes ricinus*, *Hyalomma anatolicum*, *Rhipicephalus microplus*, *Rhipicephalus sanguineus*, *Dermacentor albipictus*, *Dermacentor reticulatus*, *Varroa destructor*, *Tetranychus urticae*, *Aculops lycopersici*, *Phytoseiulus persimilis*, *Pneumolaelaps niutirani* |

### 2a efficacy

| Host / pest (from abstract) | Delivery (detected) | Mortality | LT/LC | Colony / nest | Study |
|---|---|---|---|---|---|
| Bactrocera dorsalis (oosterse fruitvlieg) | contaminated_forager |  |  | horizontal transmission of conidia to non-exposed individuals | [Xie2026](https://doi.org/10.21203/rs.3.rs-8322768/v1) |
| Monochamus alternatus (Japanse geelschildboktor) | trap |  | LT50 = 6 ;  LC50 = 9 |  | [Zhang2025](https://doi.org/10.3390/insects16101045) |
| Schistocerca gregaria (woestijnsprinkhaan) | bait_station | mortality ranging from 63 to 100% |  |  | [Mwikali2025](http://europepmc.org/abstract/AGR/IND608793514) |
| Schistocerca gregaria (woestijnsprinkhaan) | bait_station, foliar_spray | 90 % mortality |  |  | [Mwikali2024](https://doi.org/10.1016/j.biocontrol.2024.105642) |
| Lycorma delicatula (spotted lanternfly) | trap, foliar_spray | 39.7%, with higher mortality |  |  | [Keller2023](https://doi.org/10.1093/jee/toad121) |
| Galleria mellonella (grote wasmot) | bait_station, endophytic | mortality rate of Galleria melonella (100% |  |  | [Geremew2023](https://doi.org/10.12688/f1000research.134020.5) |
| Rhynchophorus ferrugineus (rode palmkever) | trap, foliar_spray | 100% mortality ;  caused 100% mortality | LC50 of neem-based insecticide |  | [Hajjar2021](http://europepmc.org/abstract/AGR/IND607523531) |
| Ostrinia nubilalis (Europese maïsboorder) | bait_station | mortality of larvae was in the range 34% | LT50 was estimated to 5 ;  LC50 were estimated in range 7 |  | [Medo2021](https://doi.org/10.1111/jen.12806) |
| Hypothenemus hampei (coffee berry borer) | trap, foliar_spray | 20-25% mortality ;  resulted in 20-25% mortality |  |  | [Wraight2021](https://doi.org/10.1016/j.biocontrol.2021.104587) |
| Ceratitis capitata (Middellandse-zeevlieg) | bait_station | mortality rates up to 91% |  |  | [Hallouti2020](https://doi.org/10.1186/s12898-020-00334-2) |
| Spodoptera frugiperda (legerrups) | trap, contaminated_forager |  |  | horizontal transmission of the inoculum among S | [Akutse2020](https://doi.org/10.1016/j.jip.2020.107477) |
| Alphitobius diaperinus (piepschuimkever) | bait_station, contaminated_forager |  |  | Horizontal transmission of the Unioeste 04 strain through contaminated living A | [Hassemer2020](https://doi.org/10.1016/j.biocontrol.2020.104326) |
| Dermanyssus gallinae (vogel-luismijt) | autodissemination, trap | mortalities by the fungus were higher than 70% |  |  | [Nascimento2020](https://doi.org/10.1007/s10493-020-00466-6) |
| Anastrepha ludens (Mexican fruit fly) | autodissemination, trap, contaminated_forager, SIT_vector |  |  | horizontal transmission in Anastrepha ludens ;  que (SIT) could be enhanced by augmenting  | [Montoya2020](https://doi.org/10.1111/jen.12766) |
| Rhipicephalus microplus (runderteek) | bait_station | 86.7% and 60% mortality ;  53.5% mortality | LC50 of 2 107 and LC99 of 7 108 conidia/ml |  | [Fernandez-Salas2018](https://doi.org/10.1645/17-162) |
| Hypothenemus hampei (coffee berry borer) | autodissemination, trap | 88.5% confirmed mortality |  |  | [Mota2017](https://doi.org/10.1016/j.biocontrol.2017.05.007) |
| Musca domestica (huisvlieg) | bait_station | mortality percentages ranging from 53.00% | LC50 values and a shorter lethal time | fecundity and longevity | [Farooq2016](https://doi.org/10.1016/j.bjm.2016.06.002) |
| Rhynchophorus ferrugineus (rode palmkever) | trap, contaminated_forager | 100% mortality ;  caused 100% mortality | LC50 of B ;  LT50 was 13 |  | [Hajjar2015](https://doi.org/10.1093/jee/tou055) |
| Cosmopolites sordidus | trap | mortality, leading to 40% ;  90% of adult mortality ;  20% mortality |  |  | [Fancelli2013](https://doi.org/10.1155/2013/184756) |
| Musca domestica (huisvlieg) | bait_station, trap | 100% mortality ;  100 % mortality ;  30.6 % (after 12-months storage) mortality ;  19.9% h |  |  | [Mishra2013](https://doi.org/10.1007/s00436-013-3529-6) |
| Tenebrio molitor (meeltor) | bait_station | mortality on thrips (some causing 88% ;  mortality levels against whiteflies (75% ;  88% m |  |  | [Sanchez-Pena2011](https://doi.org/10.1673/031.011.0101) |
| Hyalomma anatolicum | bait_station | 90% mortality |  |  | [Sun2011](https://doi.org/10.1016/j.vetpar.2011.03.027) |
| Musca domestica (huisvlieg) | bait_station | 90% mortality |  |  | [Lecuona2005](https://doi.org/10.1093/jmedent/42.3.332) |
| Alphitobius diaperinus (piepschuimkever) | trap, direct_contact_bioassay |  | LC50 = 1 ;  LC90 = 9 ;  LC50 = 2 ;  LC90 = 4 |  | [Geden1998](https://doi.org/10.1006/bcon.1998.0647) |

Note: 1 additional `02a`-tagged abstracts report mortality/LT under foliar, contact, endophytic, or unclear delivery only (see extract CSV). 50 `02a` rows had no mortality/LT/colony string in the abstract.

### 2b strains-traits

| Traits (detected) | Virulence link | Carrier / surface context | Study |
|---|---|---|---|
| adhesion, virulence | yes | oil, encapsulation_hydrogel | [Kolanchi2026](https://doi.org/10.1016/j.micpath.2025.108272) |
| virulence | yes | oil | [Riaz2026](https://doi.org/10.3390/insects17060622) |
| protease, virulence | yes | protein_bait | [Tang2025](https://doi.org/10.1073/pnas.2419343122) |
| virulence, spore_production | yes | trap_surface | [Geremew2023](https://doi.org/10.12688/f1000research.134020.5) |
| virulence | yes | oil | [Zeina2022](https://doi.org/10.1007/s10493-021-00674-8) |
| virulence | yes | oil | [Awan2021](https://doi.org/10.1002/ps.6429) |
| virulence | yes | aqueous | [Medo2021](https://doi.org/10.1111/jen.12806) |
| virulence | yes | aqueous, electrostatic | [Muniz2020](https://doi.org/10.1016/j.jip.2020.107391) |
| virulence | yes | oil | [Dembilio2018](https://doi.org/10.1002/ps.4888) |
| virulence | yes | trap_surface | [Sanchez-Pena2011](https://doi.org/10.1673/031.011.0101) |
| virulence | yes |  | [Forlani2011](https://doi.org/10.2147/rrtm.s22961) |
| thermotolerance | unclear | oil, granular | [Kim2010](https://doi.org/10.4014/jmb.1005.05023) |
| virulence | yes | trap_surface | [Lecuona2005](https://doi.org/10.1093/jmedent/42.3.332) |

### 2c mechanics

| Carriers | Claims | Device / delivery | Study |
|---|---|---|---|
| protein_bait | germination, persistence, sporulation | contaminated_forager | [Xie2026](https://doi.org/10.21203/rs.3.rs-8322768/v1) |
|  | transfer | autodissemination, trap | [Paris2026](https://doi.org/10.1093/jme/tjag078) |
| encapsulation_hydrogel, aqueous |  | bait_station, trap | [Friuli2025](https://doi.org/10.1002/ps.8476) |
|  | persistence, transfer | trap | [Zhang2025](https://doi.org/10.3390/insects16101045) |
| protein_bait |  | bait_station | [Tang2025](https://doi.org/10.1073/pnas.2419343122) |
| encapsulation_hydrogel, granular, mineral_carrier |  | bait_station | [Duarte2024](https://doi.org/10.21203/rs.3.rs-4331320/v1) |
|  | persistence | trap, foliar_spray | [Keller2023](https://doi.org/10.1093/jee/toad121) |
|  | germination | bait_station, endophytic | [Geremew2023](https://doi.org/10.12688/f1000research.134020.5) |
|  | transfer | SIT_vector | [RamirezyRamirez2022](http://europepmc.org/abstract/AGR/IND607628548) |
| aqueous |  | trap, foliar_spray | [Hajjar2021](http://europepmc.org/abstract/AGR/IND607523531) |
| aqueous |  | bait_station | [Medo2021](https://doi.org/10.1111/jen.12806) |
|  | transfer | autodissemination, trap | [Buckner2021](https://doi.org/10.2987/21-7038) |
|  | germination | trap, contaminated_forager | [Akutse2020](https://doi.org/10.1016/j.jip.2020.107477) |
|  | viability | autodissemination, trap | [Nascimento2020](https://doi.org/10.1007/s10493-020-00466-6) |
|  | transfer | autodissemination, trap, contaminated_forager | [Srei2020](https://doi.org/10.1093/jee/toaa226) |
|  | transfer | autodissemination, trap, contaminated_forager, SIT_vector | [Montoya2020](https://doi.org/10.1111/jen.12766) |
|  | transfer | autodissemination, trap | [Mota2017](https://doi.org/10.1016/j.biocontrol.2017.05.007) |
|  | transfer | autodissemination, trap | [Buckner2017](https://doi.org/10.2987/17-6642R.1) |
| encapsulation_hydrogel |  | bait_station, soil_drench | [Vemmer2016](https://doi.org/10.1002/ps.4245) |
| aqueous |  | trap, contaminated_forager | [Hajjar2015](https://doi.org/10.1093/jee/tou055) |
| aqueous |  | bait_station, foliar_spray | [Kavallieratos2014](https://doi.org/10.4315/0362-028x.jfp-13-196) |
|  | adhesion, transfer | autodissemination, trap | [Snetselaar2014](https://doi.org/10.1186/1756-3305-7-200) |
| oil, encapsulation_hydrogel | viability, germination | bait_station, trap | [Mishra2013](https://doi.org/10.1007/s00436-013-3529-6) |
|  | viability | trap | [Fang2012](https://doi.org/10.1371/journal.pone.0043069) |
|  | adhesion, germination, transfer | autodissemination, trap | [Lyons2012](https://doi.org/10.1603/ec12325) |
| oil | transfer | autodissemination | [Barbarin2012](https://doi.org/10.1016/j.jip.2012.04.009) |
|  | persistence | trap, soil_drench | [Garrido-Jurado2011](https://doi.org/10.1016/j.biocontrol.2011.07.001) |
|  | transfer | autodissemination, contaminated_forager, foliar_spray | [Forlani2011](https://doi.org/10.2147/rrtm.s22961) |
| granular |  | bait_station | [Geden2003](https://doi.org/10.1603/0022-0493-96.5.1602) |
|  | transfer | autodissemination, trap | [Dowd2003](https://doi.org/10.1080/0958315021000054395) |
| aqueous |  | trap, direct_contact_bioassay | [Geden1998](https://doi.org/10.1006/bcon.1998.0647) |
| oil, wettable_powder, granular |  | trap, soil_drench | [Parker1997](https://doi.org/10.1006/bcon.1997.0516) |
| oil |  | bait_station, foliar_spray | [Inglis1996](https://doi.org/10.1080/09583159650039511) |
|  | transfer | autodissemination, trap | [Vega1995](https://doi.org/10.1006/bcon.1995.1064) |

## 3 autodissemination-social

| Pathway | Host / pest | Mortality | Nest / social outcome | Study |
|---|---|---|---|---|
| horizontal_transmission | Bactrocera dorsalis (oosterse fruitvlieg) |  | horizontal transmission of conidia to non-exposed individuals | [Xie2026](https://doi.org/10.21203/rs.3.rs-8322768/v1) |
| horizontal_transmission | Zeugodacus cucurbitae (melon fly) |  | Horizontal Transmission of Beauveria bassiana Against Zeugodacus cucurbitae with | [Fu2026](https://doi.org/10.3390/insects17050475) |
| social_behaviour | Reticulitermes chinensis (termite sp) |  | allogrooming behavior among termites | [Xiong2026](https://doi.org/10.1002/ps.71081) |
| horizontal_transmission | Bio efficacy; Indigenous isolates | 98% mortality | horizontal transmission of fruit fly adult was tested achieving highest mortalit | [Riaz2025](https://doi.org/10.21203/rs.3.rs-7259186/v1) |
| social_behaviour | Biopesticides have; Polistes dominula (Franse veldwesp) |  | Nestmate Recognition in a Social Paper Wasp ;  ntomopathogenic fungus Beauveria  | [DeFazi2025](https://doi.org/10.1002/tox.24547) |
| social_behaviour | Reticulitermes chinensis (termite sp); Termites play |  | allogrooming, trophallaxis, vibration, cannibalism, burial, locomotion, and fora | [Hassan2025](https://doi.org/10.1016/j.jip.2025.108419) |
| horizontal_transmission | Rhynchophorus ferrugineus (rode palmkever) | 60-88% female mortality | horizontal transmission of fungal conidia from an egg-laying surface to the fema | [Ment2023](https://doi.org/10.3390/insects14120918) |
| autodissemination_device, horizontal_transmission, SIT | Horizontal transmission; Ceratitis capitata (Middellandse-zeevlieg) |  | Horizontal transmission of Beauveria bassiana spores using infected males and in | [Galvez2022](https://doi.org/10.21203/rs.3.rs-2180398/v1) |
| horizontal_transmission | Zeugodacus cucurbitae (melon fly) | mortalities of 94, 87, and 81% ;  mortality of 74% ;  67% mortality | Horizontal Transmission, and Compatability with Cuelure ;  For horizontal transm | [Onsongo2022](https://doi.org/10.3390/insects13100859) |
| horizontal_transmission | Pristiphora abietina; Chemical pesticides | 59-100% mortality ;  caused 59-100% mortality | horizontal transmission in the pest population was shown | [Biryol2021](https://doi.org/10.1111/eea.13035) |
| horizontal_transmission | Bactrocera zonata (peach fruit fly) |  | horizontal transmission, greenhouse, and field-cage efficacy of locally isolated | [Usman2021](https://doi.org/10.3390/microorganisms9081791) |
| horizontal_transmission | Kuschelorhynchus macadamiae; Our previous | mortality of healthy adults reached 100% ;  mortality of adults was 80 | horizontal transmission of both fungal species to healthy weevils from both infe | [Khun2021](https://doi.org/10.1038/s41598-021-81647-0) |
| horizontal_transmission | Trialeurodes vaporariorum (kaswittevlieg) | mortality of 45-93% ;  mortalities of 82, 91 and 93% | horizontal transmission of Metarhizium anisopliae by the adults of the greenhous | [Paradza2021](https://doi.org/10.1016/j.heliyon.2021.e08277) |
| horizontal_transmission | Spodoptera frugiperda (legerrups) |  | horizontal transmission of the inoculum among S | [Akutse2020](https://doi.org/10.1016/j.jip.2020.107477) |
| horizontal_transmission | Alphitobius diaperinus (piepschuimkever) |  | Horizontal transmission of the Unioeste 04 strain through contaminated living A | [Hassemer2020](https://doi.org/10.1016/j.biocontrol.2020.104326) |
| autodissemination_device, horizontal_transmission | Agrilus planipennis (Aziatische essenprachtkever); Emerald ash |  | Horizontal Transmission of the Entomopathogenic Fungal Isolate INRS-242 of Beauv | [Srei2020](https://doi.org/10.1093/jee/toz256) |
| horizontal_transmission | Thaumatotibia leucotreta (Afrikaanse fruitmot) | 50% mortality | Horizontal Transmission, and Their Effects on Reproductive Potential of Thaumato | [Mkiga2020](https://doi.org/10.1093/jee/toz342) |
| autodissemination_device, horizontal_transmission, SIT | Anastrepha ludens (Mexican fruit fly) |  | horizontal transmission in Anastrepha ludens ;  que (SIT) could be enhanced by a | [Montoya2020](https://doi.org/10.1111/jen.12766) |
| horizontal_transmission | Psoroptes ovis; Previous studies | 100% mortality ;  resulted in 100% mortality | horizontal transmission between Psoroptes ovis mites, but we still lack informat | [Jiang2019](https://doi.org/10.1016/j.biocontrol.2019.01.010) |
| social_behaviour | Eusocial insects; Camponotus could |  | allogrooming and trophallaxis, during the days after exposure ;  but none of the | [Bos2019](https://doi.org/10.3390/insects10090271) |
| social_behaviour | Natural biocide; Honeybee colonies |  | nestmate recognition in honeybees ;  pact of the fungus Beauveria bassiana on ho | [Cappa2019](https://doi.org/10.1038/s41598-019-38963-3) |
| autodissemination_device, horizontal_transmission | Spodoptera frugiperda (legerrups); All isolates |  | horizontal transmission of the entomopathogen male-female in three ratios (1:5,  | [Gutirrez-Crdenas2019](http://europepmc.org/abstract/AGR/IND606489546) |
| autodissemination_device, horizontal_transmission | Vuillemin strain |  | horizontal transmission of Beauveria bassiana (Balsamo) Vuillemin strain Bb-M to | [Suarez-Nunez2017](http://europepmc.org/abstract/AGR/IND605947294) |
| horizontal_transmission | Musca domestica (huisvlieg) | 90%, and the mortality | Horizontal Transmission of Beauveria bassiana (Hypocreales: Cordycipitaceae) and | [Carcamo2015](https://doi.org/10.1093/jee/tov163) |
| social_behaviour | Foster carers; Social organisms |  | trophallaxis and allogrooming ;  whether colonies contain a single or multiple q | [Purcell2014](https://doi.org/10.1098/rspb.2014.1338) |
| horizontal_transmission | Mycosis inhibits; Melanoplus sanguinipes |  | horizontal transmission of Microsporida and entomopathogenic fungi | [Jaronski2013](https://doi.org/10.1673/031.013.12201) |
| autodissemination_device, horizontal_transmission | Triatoma infestans; Chagas disease |  | horizontal transmission of the entomopathogenic fungus Beauveria bassiana to the | [Forlani2011](https://doi.org/10.2147/rrtm.s22961) |
| horizontal_transmission, SIT | Horizontal transmission; Anastrepha ludens (Mexican fruit fly) | mortality = 98.7% ;  mortality = 99.3% | Horizontal transmission of Beauveria bassiana in Anastrepha ludens (Diptera: Tep | [Toledo2007](https://doi.org/10.1603/0022-0493(2007)100[291:htobbi]2.0.co;2) |
| horizontal_transmission | Horizontal transmission; Ips typographus (letterzetter) | mortalities at 7 days were 83, 77 and 75% ;  mortality of treated and  | Horizontal transmission of the entomopathogenic fungus Beauveria bassiana among  | [Kreutz2004](https://doi.org/10.1080/788222844) |
| autodissemination_device, horizontal_transmission | Horizontal transmission | 100% mortality ;  85% mortality ;  93% mortality ;  resulted in 85% mo | Horizontal transmission of entomopathogenic fungi by the diamondback moth | [Furlong2001](https://doi.org/10.1006/bcon.2001.0981) |
| horizontal_transmission | Horizontal transmission |  | Horizontal transmission of Beauveria bassiana (Bals | [Long2000](https://doi.org/10.1046/j.1461-9563.2000.00046.x) |
| horizontal_transmission |  |  | horizontal transmission | [Long2000](https://doi.org/10.1046/j.1461-9563.2000.00047.x) |
| autodissemination_device | Semifield evaluation; Aedes notoscriptus |  |  | [Paris2026](https://doi.org/10.1093/jme/tjag078) |
| autodissemination_device | Culex quinquefasciatus (southern house mosquito) |  |  | [Buckner2025](https://doi.org/10.1093/jme/tjae124) |
| autodissemination_device | Liriomyza sativae |  |  | [Zhang2025](http://europepmc.org/abstract/AGR/IND609241699) |
| SIT | Dual suppression; Glossina pallidipes (tsetse sp) |  |  | [Ombura2024](https://doi.org/10.3389/fmicb.2024.1472324) |
| autodissemination_device | Australian backyard; Aedes notoscriptus |  |  | [Paris2023](https://doi.org/10.1093/jme/tjad099) |
| autodissemination_device, SIT | Sexual performance; Ceratitis capitata (Middellandse-zeevlieg) |  |  | [RamirezyRamirez2022](http://europepmc.org/abstract/AGR/IND607628548) |
| autodissemination_device | Aedes aegypti (gelekoortsmug); Zika viruses |  |  | [Buckner2021](https://doi.org/10.2987/21-7038) |
|  | Hypothenemus hampei (coffee berry borer) | 20-25% mortality ;  resulted in 20-25% mortality |  | [Wraight2021](https://doi.org/10.1016/j.biocontrol.2021.104587) |
| autodissemination_device | Aedes aegypti (gelekoortsmug) |  |  | [Reyes-Villanueva2021](https://doi.org/10.3389/fcimb.2021.616679) |
| autodissemination_device | Dermanyssus gallinae (vogel-luismijt) | mortalities by the fungus were higher than 70% |  | [Nascimento2020](https://doi.org/10.1007/s10493-020-00466-6) |
| autodissemination_device | Emerald ash |  |  | [Srei2020](https://doi.org/10.1093/jee/toaa226) |
| autodissemination_device | Rhipicephalus sanguineus (hondenteek) |  |  | [Weeks2019](https://doi.org/10.1111/mve.12426) |
| autodissemination_device | Otiorhynchus sulcatus (gegroefde lapsnuitkever); Vine weevil | 70-90% mortality ;  caused 70-90% mortality |  | [Pope2018](https://doi.org/10.1016/j.jip.2018.04.002) |

Note: 12 further rows with abstract endpoints are in the extract CSV only.

## 4 nontarget-ecotox

| Non-target taxa | Exposure route | Effect direction | Study |
|---|---|---|---|
| Apis, predator_parasitoid, human | foliar_spray | adverse_or_mortality_mentioned | [Unknown2026](https://doi.org/10.21203/rs.3.rs-9264759/v1) |
| other_beneficial | trap | adverse_or_mortality_mentioned | [Zhang2025](https://doi.org/10.3390/insects16101045) |
| other_beneficial | unclear | adverse_or_mortality_mentioned | [DeFazi2025](https://doi.org/10.1002/tox.24547) |
| Bombus | SIT_vector, foliar_spray | adverse_or_mortality_mentioned | [Kapongo2025](https://doi.org/10.3389/finsc.2025.1468262) |
| other_beneficial | bait_station, foliar_spray | adverse_or_mortality_mentioned | [Mwikali2024](https://doi.org/10.1016/j.biocontrol.2024.105642) |
| other_beneficial, human | bait_station | adverse_or_mortality_mentioned | [Konopicka2024](https://doi.org/10.1093/jambio/lxae213) |
| Bombus, other_beneficial, human | SIT_vector, foliar_spray | adverse_or_mortality_mentioned | [Kotomale2024](https://doi.org/10.20944/preprints202408.0225.v1) |
| predator_parasitoid, other_beneficial | unclear | compatible_or_low_effect, adverse_or_mortality_mentioned | [DeSouza2023](https://doi.org/10.1007/s11356-023-29770-5) |
|  | trap, foliar_spray | adverse_or_mortality_mentioned | [Keller2023](https://doi.org/10.1093/jee/toad121) |
| Apis, Bombus, other_beneficial | unclear | adverse_or_mortality_mentioned | [Leite2022](https://doi.org/10.3390/microorganisms10091800) |
| Apis, native_bee | unclear |  | [Almeida2022](https://doi.org/10.1016/j.chemosphere.2021.132147) |
| Apis | unclear | adverse_or_mortality_mentioned | [Omuse2022](https://doi.org/10.1093/jee/toab211) |
| Apis | unclear | adverse_or_mortality_mentioned | [Rosana2021](https://doi.org/10.1007/s00253-021-11172-7) |
| other_beneficial | autodissemination, trap, contaminated_forager, SIT_vector |  | [Montoya2020](https://doi.org/10.1111/jen.12766) |
| Apis | unclear | compatible_or_low_effect | [Peng2020](https://doi.org/10.1002/ps.5803) |
| Apis | unclear | compatible_or_low_effect | [Carlesso2020](https://doi.org/10.1038/s41598-020-76852-2) |
| Apis | unclear | adverse_or_mortality_mentioned | [Cappa2019](https://doi.org/10.1038/s41598-019-38963-3) |
| Apis | unclear |  | [Challa2019](https://doi.org/10.1016/j.envpol.2019.03.048) |
| other_beneficial | unclear | compatible_or_low_effect, adverse_or_mortality_mentioned | [Bordalo2019](https://doi.org/10.1016/j.scitotenv.2019.134155) |
| Apis, other_beneficial | foliar_spray | adverse_or_mortality_mentioned | [Portilla2017](http://europepmc.org/abstract/AGR/IND605922757) |
| Apis, Bombus, other_beneficial | unclear | adverse_or_mortality_mentioned | [Toledo-Hernandez2016](https://doi.org/10.1093/jee/tow064) |
| Apis | unclear |  | [Romo-Chacon2016](http://europepmc.org/abstract/AGR/IND605588787) |
| other_beneficial | unclear | adverse_or_mortality_mentioned | [Reddy2016](https://doi.org/10.1016/j.toxrep.2016.05.003) |
|  | soil_drench | adverse_or_mortality_mentioned | [Swiergiel2016](https://doi.org/10.1111/1744-7917.12233) |
| Apis | unclear |  | [Kim2015](https://doi.org/10.1016/j.cbpb.2014.11.010) |
| Apis | unclear |  | [Kim2013](https://doi.org/10.1016/j.toxicon.2013.09.017) |
| Bombus | direct_contact_bioassay | adverse_or_mortality_mentioned | [Ramanaidu2013](https://doi.org/10.1002/ps.3456) |
| Apis | unclear | adverse_or_mortality_mentioned | [Ahmed2013](https://doi.org/10.3923/pjbs.2013.819.825) |
| Bombus, predator_parasitoid, other_beneficial | SIT_vector |  | [Shipp2012](https://doi.org/10.1016/j.biocontrol.2012.07.008) |
| Apis | unclear | adverse_or_mortality_mentioned | [Hamiduzzaman2012](https://doi.org/10.1016/j.jip.2012.09.001) |
| Apis | unclear |  | [Meikle2012](https://doi.org/10.1016/j.biocontrol.2011.12.004) |
| other_beneficial | trap, soil_drench | adverse_or_mortality_mentioned | [Garrido-Jurado2011](https://doi.org/10.1016/j.biocontrol.2011.07.001) |
| Bombus | unclear | adverse_or_mortality_mentioned | [Mommaerts2009](https://doi.org/10.1002/ps.1778) |
| Bombus | unclear | adverse_or_mortality_mentioned | [Kapongo2008](https://doi.org/10.1016/j.biocontrol.2008.05.008) |
| Apis | unclear | compatible_or_low_effect | [Meikle2008](https://doi.org/10.1007/s10493-008-9160-z) |
| Apis | unclear |  | [Al-MazraAwi2007](https://doi.org/10.1080/09583150701484759) |
| Apis | unclear |  | [Meikle2007](https://doi.org/10.1603/0022-0493(2007)100[1:dasoae]2.0.co;2) |
| Apis, predator_parasitoid, other_beneficial, human | unclear | compatible_or_low_effect, adverse_or_mortality_mentioned | [Zimmermann2007](https://doi.org/10.1080/09583150701309006) |
| Bombus | unclear | adverse_or_mortality_mentioned | [Al-mazraawi2006](https://doi.org/10.1016/j.biocontrol.2005.11.014) |
| Apis | unclear | adverse_or_mortality_mentioned | [Muerrle2006](https://doi.org/10.1093/jee/99.1.1) |

## 5 regulatory-policy

| Instruments | Geography | Trap/bait coverage in abstract | Study |
|---|---|---|---|
| EFSA, EU_1107_2009, active_substance, dossier_RMS | EU | not_stated_in_abstract | [Authority2013](https://doi.org/10.2903/j.efsa.2013.3031) |
| EFSA, EU_1107_2009, active_substance, dossier_RMS | EU | not_stated_in_abstract | [European2017](https://doi.org/10.2903/j.efsa.2017.4831) |
| EFSA, EU_1107_2009, active_substance, dossier_RMS | EU | not_stated_in_abstract | [Anastassiadou2020](https://doi.org/10.2903/j.efsa.2020.6295) |
| EFSA, EU_1107_2009, active_substance, dossier_RMS | EU | not_stated_in_abstract | [Arena2018](https://doi.org/10.2903/j.efsa.2018.5230) |

## 6 background-proxies

n = 0 (narrow screen did not park background/keratitis here; Vespidae proxy PDFs moved to `00-key-papers` and `07-vespideae-biocontrol`).

## 0 key-papers (Beauveria + Vespidae)

| Cite | Taxon | Theme | PDF |
|---|---|---|---|
| Poidatz2018 | Vespa_velutina | beauveria_vespidae | yes |
| Poidatz2019 | Vespa_velutina | beauveria_vespidae | yes |
| Merino2007 | Vespidae | beauveria_vespidae | yes |
| Reason2022 | Vespidae | beauveria_vespidae | yes |
| vanZyl2023 | Vespidae | beauveria_vespidae | yes |
| Rose1999 | Vespidae | beauveria_vespidae | yes |
| Brownbridge2009 | Vespidae | beauveria_vespidae | yes |
| deSouza2023 | Vespidae | beauveria_vespidae | yes |
| MayorgaCh2021 | Vespidae | beauveria_vespidae | no (CSV-only) |
| Cappa2024 | Vespidae | beauveria_vespidae | no (Phase 2 include; PDF not filed) |
| DeFazi2025 | Vespidae | beauveria_vespidae | no (Phase 2 include; PDF not filed) |

## 7 vespideae-biocontrol

Non-Bb microorganisms on Vespidae plus chemical trap/bait delivery proxies. See `input-phase2/07-vespideae-biocontrol/extract.csv` (18 rows; 17 PDFs filed). CSV-only: PathogenOcc2024 (`10.1002/ps.8325`).
