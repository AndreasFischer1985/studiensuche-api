# Arbeitsagentur Studiensuche API 
Die Bundesagentur für Arbeit verfügt über eine der größten Datenbanken für Studienangebote in Deutschland. Obwohl sie vollständig staatlich ist und es sich dabei um einen sehr spannenden Basisdatensatz handelt, mit dem viele Analysen möglich wären, bietet die Bundesagentur für Arbeit dafür bis heute keine offizielle API an.


## Authentifizierung
Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs.
Client Credentials sind, wie sich z.B. einem GET-request an https://web.arbeitsagentur.de/studiensuche/suche entnehmen lässt, folgende:

**client_id:** 5aee2cfe-1709-48a9-951d-eb48f8f73a74

**client_secret:** 3309a57a-9214-40db-9abe-28b1bb30c08c

**grant_type:** client_credentials

Die Credentials sind im body eines POST-request an https://rest.arbeitsagentur.de/oauth/gettoken_cc zu senden.

```bash
token=$(curl \
-d "client_id=5aee2cfe-1709-48a9-951d-eb48f8f73a74&client_secret=3309a57a-9214-40db-9abe-28b1bb30c08c&grant_type=client_credentials" \
-X POST 'https://rest.arbeitsagentur.de/oauth/gettoken_cc' |grep -Eo '[^"]{500,}'|head -n 1)
```

Der generierte Token muss bei folgenden GET-requests an https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote im header als 'OAuthAccessToken' inkludiert werden.


## Studiensuche

**URL:** https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote


Die Studiensuche ermöglicht, verfügbare Studienangebote mit verschiedenen GET-Parametern zu filtern. In der Regel ist dabei die Angabe mindestens eines Suchwortes (sw), Studienfeldes (sfe) oder eines Studienfachs (sfa) erforderlich. Eine Ausnahme von dieser Regel besteht beispielsweise darin, den Filter zum Studienmodell (smo) auf 5 (=Duales Studium) zu setzen.


### Filter


**Parameter:** *sw* (Optional)

Suchwort, z.B. Informatikberufe


**Parameter:** *sfa* (Optional)

Studienfach-ID, z.B. 93683 für Bioinformatik


**Parameter:** *sfe* (Optional)

93574, 93575, 93581, 93583, 93584, 93592, 93593, 93598, 93611, 93621, 93625, 93627, 93638, 93648, 93649, 93650, 93651, 93659, 93661, 93677, 93685, 93690, 93694, 93696, 93698, 93699, 93701, 93705, 93713, 93718, 93719, 93720, 93724, 93733, 93736, 93739, 93751, 93757, 93767, 93772, 93774, 93795, 93796, 93797, 93799, 93802, 93804, 93813, 93814, 93815, 93817, 93818, 93819, 93821, 93825, 93828, 93836, 93837, 93842, 93846, 93847, 93850, 93853, 93858, 93861, 93871, 93888, 93889, 93890, 93891, 93896, 93900, 93901, 93904, 93907, 93909, 93911, 93914, 93915, 93918, 93928, 93935, 93936, 93940, 93946, 93953, 93958, 93959, 93970, 93977, 93979, 93986, 93988, 93989, 93995, 93999, 94000, 94008, 94010, 94014, 94020, 94030, 94033, 94037, 94041, 94056, 94063, 94065, 94069, 94087, 94098, 94101, 94114, 94116, 94120, 94121, 94122, 94130, 94142, 94143, 94144, 94145, 94158, 94163, 94170, 94175, 94178, 94179, 94187, 94197, 94204, 94217, 94221, 94224, 94228, 94230, 94231, 94237, 94240, 94242, 94246, 94249, 94252, 94253, 94256, 94257, 94258, 94262, 94269, 94284, 94299, 94303, 94304, 94307, 94310, 94319, 94321, 94322, 94324, 94327, 94328, 94329, 94330, 94333, 94334, 94346, 94348, 94350, 94352, 94357, 94358, 94362, 94363, 94373, 94374, 94375, 94378, 94379, 94383, 94384, 94393, 94394, 94398, 94403, 94405, 94406, 94408, 94412, 94420, 94422, 128341, 130047, 130048

dkzIds einer Studienfeld(gruppe), idR. zwei Semikolon-getrennte Werte je Studienfeld(gruppe):

- 94242;93767 = Studienfelgruppe 21 - Agrar-, Forst-, Ernährungswissenschaften 
- 93701;93796 = Studienfeld 2101 - Agrarwissenschaften
- 93986;93802 = Studienfeld 2103 - Ernährungswissenschaften
- 94163;94014 = Studienfeld 2105 - Forstwissenschaften, -wirtschaft
- 93858;94010 = Studienfeld 2107 - Garten-, Landschaftsbau
- 94329;93757 = Studienfeld 2109 - Lebensmittel-, Getränketechnologie
- 93713;94327 = Studienfelgruppe 23 - Ingenieurwissenschaften
- 93936;93958 = Studienfeld 2301 - Architektur, Raumplanung
- 94030;93598 = Studienfeld 2303 - Automatisierungs-, Produktionstechnik
- 93819;93690 = Studienfeld 2305 - Bautechnik
- 93970;93853 = Studienfeld 2307 - Elektro- und Informationstechnik
- 94362;94319 = Studienfeld 2309 - Energietechnik, Energiemanagement
- 94324;94394 = Studienfeld 2311 - Fahrzeug-, Verkehrstechnik
- 93815;94121 = Studienfeld 2313 - Fertigungstechnologien
- 93751;94262 = Studienfeld 2315 - Gebäude-, Versorgungstechnik, Facility-Management
- 94420;94056 = Studienfeld 2317 - Geoinformation, Vermessung
- 94114;93999 = Studienfeld 2319 - Maschinenbau, Mechanik
- 93896;94237 = Studienfeld 2321 - Mechatronik, Mikro- und Optotechnik
- 94145;94284 = Studienfeld 2323 - Medien-, Veranstaltungstechnik
- 93584;94187 = Studienfeld 2325 - Medizintechnik, Technisches Gesundheitswesen 
- 94231;94378 = Studienfeld 2327 - Nanowissenschaften
- 94269;93918 = Studienfeld 2329 - Physikalische Technik
- 93795;93574 = Studienfeld 2331 - Produktentwicklung, Konstruktion
- 94408;93627 = Studienfeld 2333 - Qualitätsmanagement
- 93907;93772 = Studienfeld 2335 - Rohstoffgewinnung, Hüttenwesen
- 94120;94383 = Studienfeld 2337 - Sicherheit und Gefahrenabwehr, Rettungsingenieurwesen
- 94307;93592 = Studienfeld 2339 - Technik, Ingenieurwissenschaften (übergreifend)
- 94256;93861 = Studienfeld 2341 - Umwelttechnik, Umweltschutz
- 93724;94204 = Studienfeld 2343 - Verfahrens-, Chemietechnik
- 93850;94143 = Studienfeld 2345 - Werkstoff-, Materialwissenschaften
- 93814;93581 = Studienfeld 2347 - Wirtschaftsingenieurwesen, Technologiemanagement
- 93940;93593 = Studienfelgruppe 25 - Mathematik, Naturwissenschaften
- 94405;94249 = Studienfeld 2501 - Angewandte Naturwissenschaften
- 93901;93935 = Studienfeld 2503 - Bio-, Umweltwissenschaften
- 94374;93928 = Studienfeld 2505 - Chemie, Pharmazie
- 93649;94179 = Studienfeld 2507 - Geowissenschaften, -technologie
- 94116;93995 = Studienfeld 2509 - Informatik
- 94144;94403 = Studienfeld 2511 - Mathematik, Statistik
- 93825;93651 = Studienfeld 2513 - Physik
- 94175;94350 = Studienfelgruppe 27 - Medizin, Gesundheitswissenschaften, Psychologie, Sport
- 94373;93720 = Studienfeld 2701 - Biomedizin, Neurowissenschaften
- 93891;94197 = Studienfeld 2703 - Gesundheitswissenschaften
- 93698;93575 = Studienfeld 2705 - Human-, Tier-, Zahnmedizin
- 94393;93804 = Studienfeld 2707 - Psychologie
- 94098;93685 = Studienfeld 2709 - Sport
- 94037;93871 = Studienfeld 2711 - Therapien
- 93813;93914 = Studienfelgruppe 29 - Wirtschaftswissenschaften
- 94304;94384 = Studienfeld 2901 - Automobilwirtschaft
- 94228;94252 = Studienfeld 2903 - Bau-, Immobilienwirtschaft
- 94008;94158 = Studienfeld 2905 - Betriebswirtschaft
- 93659;93818 = Studienfeld 2907 - Finanz- und Rechnungswesen, Controlling, Steuern
- 93909;94020 = Studienfeld 2909 - Finanzdienstleistungen, Versicherungswirtschaft
- 93989;93846 = Studienfeld 2911 - Gesundheitsmanagement, -ökonomie
- 94087;93718 = Studienfeld 2913 - Handel, Industrie, Handwerk
- 94375;94221 = Studienfeld 2915 - Internationale Wirtschaft
- 93953;93904 = Studienfeld 2917 - Logistik, Verkehr
- 94000;93719 = Studienfeld 2919 - Management
- 93977;93736 = Studienfeld 2921 - Marketing, Vertrieb
- 93799;93739 = Studienfeld 2923 - Medienwirtschaft, -management
- 94178;93900 = Studienfeld 2925 - Personalmanagement, -dienstleistung
- 94357;94217 = Studienfeld 2927 - Tourismuswirtschaft, Sport- und Eventmanagement
- 130048;130047 = Studienfeld 2928 - Wirtschaftsinformatik
- 94033;94303 = Studienfeld 2929 - Wirtschaftswissenschaften, Volkswirtschaft
- 93648;93611 = Studienfeld 2931 - Öffentliche Verwaltung
- 94346;93837 = Studienfelgruppe 31 - Rechts-, Sozialwissenschaften
- 94240;93650 = Studienfeld 3101 - Arbeitsmarktmanagement
- 93889;93915 = Studienfeld 3103 - Politikwissenschaften
- 94352;94358 = Studienfeld 3105 - Rechtswissenschaften
- 94258;93959 = Studienfeld 3107 - Sozialwesen
- 94348;93694 = Studienfeld 3109 - Sozialwissenschaften, Soziologie
- 93696;94069 = Studienfelgruppe 33 - Erziehungs-, Bildungswissenschaften, Lehrämter
- 94363;94142 = Studienfeld 3301 - Erziehungs-, Bildungswissenschaften
- 94333;94334 = Studienfeld 3303 - Lehrämter
- 93621;93661 = Studienfelgruppe 35 - Sprach-, Kulturwissenschaften
- 94101;93828 = Studienfeld 3501 - Altertumswissenschaften, Archäologie
- 93638;94412 = Studienfeld 3503 - Anglistik, Amerikanistik
- 93842;94328 = Studienfeld 3505 - Archiv, Bibliothek, Dokumentation
- 94321;93583 = Studienfeld 3507 - Außereuropäische Sprachen und Kulturen
- 94322;94253 = Studienfeld 3509 - Germanistik
- 93911;94041 = Studienfeld 3511 - Geschichtswissenschaften
- 93817;94122 = Studienfeld 3513 - Jüdische Studien, Judaistik
- 94246;94330 = Studienfeld 3515 - Kleinere europäische Sprachen und Kulturen
- 93888;93821 = Studienfeld 3517 - Kommunikation und Medien
- 93699;94398 = Studienfeld 3519 - Kulturwissenschaften
- 128341 = Studienfeld 3520 - Liberal Arts
- 93988;93836 = Studienfeld 3521 - Philosophie, Theologie, Religionspädagogik
- 94224;94063 = Studienfeld 3523 - Regionalwissenschaften
- 93797;93946 = Studienfeld 3525 - Romanistik
- 94310;93979 = Studienfeld 3527 - Slawistik
- 93705;93677 = Studienfeld 3529 - Sprach-, Literaturwissenschaften, Dolmetschen und Übersetzen
- 94257;94170 = Studienfeld 3531 - Ältere europäische Sprachen und Kulturen
- 94130;93847 = Studienfelgruppe 37 - Kunst, Musik
- 93890;93625 = Studienfeld 3701 - Bühnenbild, Szenografie
- 93733;94379 = Studienfeld 3703 - Gestaltung, Design
- 94230;94299 = Studienfeld 3705 - Kunst
- 94065;93774 = Studienfeld 3707 - Musik
- 94406;94422 = Studienfeld 3709 - Schauspiel, Tanz, Film, Fernsehen


**Parameter:** *orte*  (Optional)

Ortsangabe nebst Postleitzahl und Koordinaten (z.B. Feucht_90537_11.224918_49.376701)


**Parameter:** *pg* (Optional)

Seite (beginnend mit 1).


**Parameter:** *uk* (Optional)
- Bundesweit
- 50
- 100
- 150
- 200

Umkreis:  Bundesweit=Bundesweit, 25=25 km, 50=50 km, 100=100 km, 150=150 km, 200=200 km.

**Parameter:** *re*  (Optional)
- BW
- BY
- BE
- BB
- HB
- HH
- HE
- MV
- NI
- NW
- RP
- SL
- SN
- ST
- SH
- TH

Region/Bundesland: BW=Baden-Württemberg, BY=Bayern, BE=Berlin, BB=Brandenburg, HB=Bremen, HH=Hamburg, HE=Hessen, MV=Mecklenburg-Vorpommern, NI=Niedersachsen, NW=Nordrhei-Westfalen, RP=Rheinland-Pfalz, SL=Saarland, SN=Sachsen, ST=Sachsen-Anhalt, SH=Schleswig-Holstein, TH=Thüringen. Mehrere Komma-getrennte Angaben möglich (z.B. re=TH,BW).


**Parameter:** *sfo* (Optional)
- 1
- 2
- 3
- 4
- 5

Studienform: 1=Vollzeitstudium, 2=Teilzeitstudium, 3=Wochenendveranstaltung, 4=Fernstudium, 5=Selbststudium. Mehrere Semikolon-getrennte Angaben möglich.


**Parameter:** *st* (Optional)
- 0
- 1

Studientyp: 0=Studiengang grundständig, 1=Studiengang weiterführend


**Parameter:** *smo* (Optional)
- 1
- 2
- 3
- 4
- 5

Studiengangmodell: 1=ausbildungsintegrierend, 2=berufsintegrierend, 3=berufsbegleitend, 4=praxisintegrierend, 5=Duales Studium allgemein. Mehrere Semikolon-getrennte Angaben möglich.


**Parameter:** *abg* (Optional)
- 0
- 1
- 2
- 3
- 4
- 10
- 12

Studiengangsabschlussgrad: 0=ohne Angabe, 1=Abschlussprüfung, 2=Bachelor, 3=Diplom, 4=Diplom(FH), 10=Master, 12=Staatsexamen


**Parameter:** *hsa* (Optional)
- 101
- 106
- 107
- 108
- 113
- 114

Hochschulart: 101=Berufsakademie/Duale Hochschule, 106=FH/FAW, 107=Kunst- und Musikhochschule, 108=Universität, 111=Verwaltungshochschule, 113=Private Hochschule. 114=Hochschule eigenen Typs. Mehrere Semikolon-getrennte Angaben möglich.


**Parameter:** *san* (Optional)

Studienanbieter-ID (z.B. 26218)


**Parameter:** *ffst* (Optional)

Eignungstest: 1=Studiencheck, 2=OSA. Mehrere Semikolon-getrennte Angaben möglich.



### Beispiel:

```bash
studienangebot=$(curl -m 60 \
-H "OAuthAccessToken: $token" \
'https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote?sw=IT-Security-Manager')
```


