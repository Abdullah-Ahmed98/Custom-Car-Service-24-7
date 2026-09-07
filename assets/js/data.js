/* =========================================================
   RoadRescue 24/7 — UK partner network + service data
   Demo dataset. Replace with a live API when going to production.
   ========================================================= */

const UK_MECHANICS = [
  { id: 1,  name: "Camden Rapid Auto",         city: "London",      area: "Camden, NW1",        lat: 51.5390, lng: -0.1426, rating: 4.9, reviews: 412, eta: 18, open: true,  phone: "+442071234501", tags: ["Mobile Mechanic", "Diagnostics", "Battery"] },
  { id: 2,  name: "Southwark Key & Lock",      city: "London",      area: "Southwark, SE1",     lat: 51.5010, lng: -0.0900, rating: 4.8, reviews: 297, eta: 24, open: true,  phone: "+442071234502", tags: ["Car Keys", "Lockout", "Immobiliser"] },
  { id: 3,  name: "Heathrow Roadside Co.",     city: "London",      area: "Hounslow, TW6",      lat: 51.4700, lng: -0.4543, rating: 4.7, reviews: 188, eta: 31, open: true,  phone: "+442071234503", tags: ["Recovery", "Tyres", "Jump Start"] },
  { id: 4,  name: "Northern Quarter Motors",   city: "Manchester",  area: "Ancoats, M4",        lat: 53.4839, lng: -2.2320, rating: 4.9, reviews: 356, eta: 16, open: true,  phone: "+441611234504", tags: ["Mobile Mechanic", "Clutch", "Brakes"] },
  { id: 5,  name: "Salford Auto Locksmiths",   city: "Manchester",  area: "Salford, M5",        lat: 53.4830, lng: -2.2900, rating: 4.8, reviews: 221, eta: 22, open: true,  phone: "+441611234505", tags: ["Car Keys", "Key Programming", "Lockout"] },
  { id: 6,  name: "Digbeth Diagnostics",       city: "Birmingham",  area: "Digbeth, B5",        lat: 52.4750, lng: -1.8850, rating: 4.7, reviews: 164, eta: 20, open: true,  phone: "+441211234506", tags: ["Diagnostics", "ECU", "Engine"] },
  { id: 7,  name: "Aston Tyre & Recovery",     city: "Birmingham",  area: "Aston, B6",          lat: 52.5060, lng: -1.8830, rating: 4.6, reviews: 133, eta: 27, open: true,  phone: "+441211234507", tags: ["Tyres", "Recovery", "Battery"] },
  { id: 8,  name: "Leith Lane Garage",         city: "Edinburgh",   area: "Leith, EH6",         lat: 55.9750, lng: -3.1700, rating: 4.9, reviews: 209, eta: 19, open: true,  phone: "+441311234508", tags: ["Mobile Mechanic", "MOT Repairs", "Diagnostics"] },
  { id: 9,  name: "Old Town Key Solutions",    city: "Edinburgh",   area: "Old Town, EH1",      lat: 55.9490, lng: -3.1890, rating: 4.8, reviews: 142, eta: 25, open: true,  phone: "+441311234509", tags: ["Car Keys", "Lockout", "Spare Keys"] },
  { id: 10, name: "Cardiff Bay Autocare",      city: "Cardiff",     area: "Butetown, CF10",     lat: 51.4650, lng: -3.1650, rating: 4.7, reviews: 176, eta: 21, open: true,  phone: "+442921234510", tags: ["Mobile Mechanic", "Battery", "Brakes"] },
  { id: 11, name: "Belfast Rapid Recovery",    city: "Belfast",     area: "Titanic Qtr, BT3",   lat: 54.6080, lng: -5.9000, rating: 4.8, reviews: 151, eta: 23, open: true,  phone: "+442890123511", tags: ["Recovery", "Jump Start", "Fuel Drain"] },
  { id: 12, name: "Leeds City Mechanics",      city: "Leeds",       area: "City Centre, LS1",   lat: 53.7990, lng: -1.5490, rating: 4.9, reviews: 288, eta: 17, open: true,  phone: "+441131234512", tags: ["Mobile Mechanic", "Diagnostics", "Suspension"] },
  { id: 13, name: "Glasgow Green Motor Aid",   city: "Glasgow",     area: "Bridgeton, G40",     lat: 55.8480, lng: -4.2200, rating: 4.7, reviews: 197, eta: 22, open: true,  phone: "+441411234513", tags: ["Recovery", "Electrical", "Battery"] },
  { id: 14, name: "Bristol Harbourside Auto",  city: "Bristol",     area: "Harbourside, BS1",   lat: 51.4490, lng: -2.5990, rating: 4.8, reviews: 168, eta: 20, open: true,  phone: "+441171234514", tags: ["Mobile Mechanic", "Engine", "Cooling"] },
  { id: 15, name: "Liverpool Docks Key Co.",   city: "Liverpool",   area: "Docklands, L3",      lat: 53.4060, lng: -2.9910, rating: 4.6, reviews: 121, eta: 26, open: true,  phone: "+441511234515", tags: ["Car Keys", "Key Programming", "Lockout"] },
  { id: 16, name: "Newcastle Quayside Garage", city: "Newcastle",   area: "Quayside, NE1",      lat: 54.9690, lng: -1.6010, rating: 4.8, reviews: 154, eta: 24, open: true,  phone: "+441911234516", tags: ["Mobile Mechanic", "Brakes", "Diagnostics"] },
  { id: 17, name: "Sheffield Steel City Auto", city: "Sheffield",   area: "Attercliffe, S9",    lat: 53.3900, lng: -1.4200, rating: 4.7, reviews: 139, eta: 23, open: true,  phone: "+441141234517", tags: ["Recovery", "Tyres", "Battery"] },
  { id: 18, name: "Nottingham Nightshift Kfz", city: "Nottingham",  area: "Sneinton, NG2",      lat: 52.9520, lng: -1.1250, rating: 4.9, reviews: 203, eta: 18, open: true,  phone: "+441151234518", tags: ["Mobile Mechanic", "Night Callout", "Electrical"] },
  { id: 19, name: "Southampton Marine Motors", city: "Southampton", area: "Ocean Village, SO14",lat: 50.8980, lng: -1.3900, rating: 4.6, reviews: 112, eta: 28, open: true,  phone: "+442381234519", tags: ["Diagnostics", "Battery", "Recovery"] },
  { id: 20, name: "Brighton Coastal Callout",  city: "Brighton",    area: "Kemptown, BN2",      lat: 50.8200, lng: -0.1300, rating: 4.8, reviews: 174, eta: 21, open: true,  phone: "+441273123520", tags: ["Mobile Mechanic", "Lockout", "Jump Start"] },
  { id: 21, name: "Leicester Ring Road Auto",  city: "Leicester",   area: "Belgrave, LE4",      lat: 52.6500, lng: -1.1200, rating: 4.7, reviews: 128, eta: 22, open: true,  phone: "+441161234521", tags: ["Recovery", "Engine", "Clutch"] },
  { id: 22, name: "Coventry Key Masters",      city: "Coventry",    area: "Foleshill, CV6",     lat: 52.4300, lng: -1.5000, rating: 4.8, reviews: 146, eta: 25, open: true,  phone: "+442476123522", tags: ["Car Keys", "Immobiliser", "Spare Keys"] }
];

/* City → coordinates, used for postcode/town lookup fallback */
const UK_PLACES = {
  "london": [51.5074, -0.1278], "manchester": [53.4808, -2.2426], "birmingham": [52.4862, -1.8904],
  "edinburgh": [55.9533, -3.1883], "glasgow": [55.8642, -4.2518], "cardiff": [51.4816, -3.1791],
  "belfast": [54.5973, -5.9301], "leeds": [53.8008, -1.5491], "bristol": [51.4545, -2.5879],
  "liverpool": [53.4084, -2.9916], "newcastle": [54.9783, -1.6178], "sheffield": [53.3811, -1.4701],
  "nottingham": [52.9548, -1.1581], "southampton": [50.9097, -1.4044], "brighton": [50.8225, -0.1372],
  "leicester": [52.6369, -1.1398], "coventry": [52.4068, -1.5197], "oxford": [51.7520, -1.2577],
  "cambridge": [52.2053, 0.1218], "york": [53.9600, -1.0873], "reading": [51.4543, -0.9781],
  "milton keynes": [52.0406, -0.7594], "aberdeen": [57.1497, -2.0943], "swansea": [51.6214, -3.9436],
  "plymouth": [50.3755, -4.1427], "norwich": [52.6309, 1.2974], "hull": [53.7457, -0.3367],
  "derby": [52.9225, -1.4746], "stoke": [53.0027, -2.1794], "wolverhampton": [52.5870, -2.1288],
  "luton": [51.8787, -0.4200], "bolton": [53.5789, -2.4297], "bradford": [53.7960, -1.7594],
  "portsmouth": [50.8198, -1.0880], "preston": [53.7632, -2.7031], "watford": [51.6565, -0.3903]
};

/* Postcode area prefix → coordinates (first 1–2 letters of a UK postcode) */
const UK_POSTCODE_AREAS = {
  AB: [57.1497, -2.0943], AL: [51.7500, -0.3360], B: [52.4862, -1.8904],  BA: [51.3800, -2.3600],
  BB: [53.7480, -2.4830], BD: [53.7960, -1.7594], BH: [50.7192, -1.8808], BL: [53.5789, -2.4297],
  BN: [50.8225, -0.1372], BR: [51.4060, 0.0150],  BS: [51.4545, -2.5879], BT: [54.5973, -5.9301],
  CA: [54.8951, -2.9382], CB: [52.2053, 0.1218],  CF: [51.4816, -3.1791], CH: [53.1900, -2.8900],
  CM: [51.7350, 0.4690],  CO: [51.8890, 0.9030],  CR: [51.3762, -0.0982], CT: [51.2800, 1.0800],
  CV: [52.4068, -1.5197], CW: [53.0980, -2.4400], DA: [51.4460, 0.2150],  DD: [56.4620, -2.9707],
  DE: [52.9225, -1.4746], DG: [55.0700, -3.6030], DH: [54.7750, -1.5750], DL: [54.5230, -1.5590],
  DN: [53.5228, -1.1285], DT: [50.7150, -2.4400], DY: [52.5120, -2.0810], E: [51.5390, 0.0100],
  EC: [51.5170, -0.0930], EH: [55.9533, -3.1883], EN: [51.6520, -0.0810], EX: [50.7184, -3.5339],
  FK: [56.0020, -3.7830], FY: [53.8175, -3.0357], G: [55.8642, -4.2518],  GL: [51.8642, -2.2380],
  GU: [51.2360, -0.5700], HA: [51.5800, -0.3400], HD: [53.6458, -1.7850], HG: [53.9920, -1.5410],
  HP: [51.7500, -0.7500], HR: [52.0567, -2.7160], HU: [53.7457, -0.3367], HX: [53.7220, -1.8590],
  IG: [51.5590, 0.0740],  IP: [52.0567, 1.1482],  IV: [57.4778, -4.2247], KA: [55.6110, -4.4980],
  KT: [51.4120, -0.3000], KY: [56.1120, -3.1600], L: [53.4084, -2.9916],  LA: [54.0470, -2.8010],
  LD: [52.2410, -3.3820], LE: [52.6369, -1.1398], LL: [53.2800, -3.8300], LN: [53.2307, -0.5406],
  LS: [53.8008, -1.5491], LU: [51.8787, -0.4200], M: [53.4808, -2.2426],  ME: [51.3900, 0.5200],
  MK: [52.0406, -0.7594], ML: [55.7860, -3.9770], N: [51.5640, -0.1050],  NE: [54.9783, -1.6178],
  NG: [52.9548, -1.1581], NN: [52.2405, -0.9027], NP: [51.5842, -2.9977], NR: [52.6309, 1.2974],
  NW: [51.5400, -0.1900], OL: [53.5409, -2.1114], OX: [51.7520, -1.2577], PA: [55.8460, -4.4240],
  PE: [52.5695, -0.2405], PH: [56.3950, -3.4300], PL: [50.3755, -4.1427], PO: [50.8198, -1.0880],
  PR: [53.7632, -2.7031], RG: [51.4543, -0.9781], RH: [51.1160, -0.1730], RM: [51.5760, 0.1830],
  S: [53.3811, -1.4701],  SA: [51.6214, -3.9436], SE: [51.4800, -0.0600], SG: [51.9020, -0.2020],
  SK: [53.4106, -2.1575], SL: [51.5100, -0.5950], SM: [51.3600, -0.1930], SN: [51.5580, -1.7800],
  SO: [50.9097, -1.4044], SP: [51.0690, -1.7940], SR: [54.9060, -1.3810], SS: [51.5400, 0.7100],
  ST: [53.0027, -2.1794], SW: [51.4600, -0.1700], SY: [52.7070, -2.7540], TA: [51.0150, -3.1000],
  TD: [55.6000, -2.4300], TF: [52.6780, -2.4450], TN: [51.1320, 0.2630],  TQ: [50.4620, -3.5250],
  TR: [50.2660, -5.0510], TS: [54.5740, -1.2350], TW: [51.4460, -0.3300], UB: [51.5400, -0.4200],
  W: [51.5140, -0.1900],  WA: [53.3900, -2.5970], WC: [51.5190, -0.1200], WD: [51.6565, -0.3903],
  WF: [53.6830, -1.4980], WN: [53.5450, -2.6320], WR: [52.1936, -2.2216], WS: [52.5860, -1.9820],
  WV: [52.5870, -2.1288], YO: [53.9600, -1.0873], ZE: [60.1550, -1.1450]
};

const SERVICE_CATALOGUE = [
  { key: "mechanic",   name: "Emergency Mobile Mechanic",  from: 65, unit: "callout", eta: "20–40 min" },
  { key: "keys",       name: "Car Key Making & Programming", from: 89, unit: "job",   eta: "30–60 min" },
  { key: "lockout",    name: "Vehicle Lockout / Unlocking", from: 55, unit: "callout", eta: "20–35 min" },
  { key: "battery",    name: "Battery Jump Start & Replace", from: 45, unit: "callout", eta: "15–30 min" },
  { key: "tyre",       name: "Puncture & Tyre Replacement",  from: 49, unit: "wheel",  eta: "25–45 min" },
  { key: "diagnostic", name: "On-Site Fault Diagnostics",    from: 59, unit: "scan",   eta: "25–40 min" },
  { key: "fuel",       name: "Wrong Fuel Drain & Flush",     from: 129, unit: "job",   eta: "35–60 min" },
  { key: "recovery",   name: "Breakdown Recovery & Towing",  from: 95, unit: "tow",    eta: "30–60 min" }
];
