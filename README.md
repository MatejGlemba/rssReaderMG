# RSS READER

Matej Glemba - Webové publikovanie - Projekt

# 1. časť RSS Reader
Link na video = https://www.youtube.com/watch?v=rug6lOErUjU&feature=youtu.be 
(az ked som ho uploadol som zistil ze tam je hudba, tak to si nemusite vsimat ;) )

Projekt bol tvorený v prostredí VSCODE s využitím jazyka Python a framework-u Django.

Najlepšie funguje portál SME.sk a CNN , BBC a Dennik N majú iné štruktúry a nenaparsuje sa všetko tak ako má.

Je možné sortovať podľa dátumu. Pokiaľ sortovanie nespraví nič, tak potrebné údaje na sortovanie chýbajú napr (CNN)

Stránka prešla W3C validátorom (Je to znázornené aj vo videu)

Stránka je responzívna (takisto to je vo videu)

# 2. časť CI Deployment
Link na video = https://youtu.be/QCkDbnUuXAw
Link na web = https://rss-reader-mg.azurewebsites.net/

Na deployment som využil platformu Azure. Kedže projekt je nakódený v Pythone vo frameworku Django, defaultne používa svoju SQLite databázu. Tá ale nie je prispôsobená na deployment, tak bolo potrebné použiť PostgreSQL, ktorý je takisto na platforme Azure.

Vo videu som spravil malú zmenu vo footri webu, následne som spravil commit a push-ol ho na github repozitár. Azure je nalinkovaný na moj repozitár a potiahol si odtial najnovšiu zmenu a spustil build. Telo buildu tvorilo vytvorenie virtualneho environmentu, instaláciu požadovaných libs, ktoré sú v priečinku requirements.txt a následne sa vložili dáta do working directory '/home/site/wwwroot'. Následne mi Azure oznámil, že build a deployment bol úspešný a pri najnovšom commite pribudol flag (Active). Refreshol som stránku a obsahovala najnovšie zmeny. 

Kód som takisto minifikoval, použitím 'from htmlmin.decorators import minified_response'. Skontrolovať si to môžte na stránke https://rss-reader-mg.azurewebsites.net/.



