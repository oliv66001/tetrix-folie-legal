# Génère le site légal de Starfuse (GitHub Pages) dans toutes les langues.
#
#   python build.py
#
# Ajouter une langue : copier un bloc de LANGS (par ex. "en"), changer le code,
# traduire les textes, relancer le script, puis publier (git add/commit/push).
# Ne pas modifier les .html à la main : ils sont réécrits à chaque génération.
import html
import os
import shutil
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://oliv66001.github.io/tetrix-folie-legal/"
GAME = "Starfuse"
EMAIL = "developpement.solution@gmail.com"
PUBLISHER = "Développement-Solution — Olivier Pagé"
ADDRESS = "20 rue Condorcet, 66330 Cabestany, France"
PAGES = ["index", "privacy", "delete-account", "contact"]


def mail(subject, body=""):
    url = f"mailto:{EMAIL}?subject={quote(subject)}"
    if body:
        url += f"&body={quote(body)}"
    return html.escape(url, quote=True)


LANGS = {
    # ------------------------------------------------------------------ FRANÇAIS
    "fr": {
        "name": "Français",
        "date": "26 octobre 2026",
        "updated": "Dernière mise à jour",
        "nav": {"index": "Accueil", "privacy": "Confidentialité",
                "delete-account": "Suppression du compte et des données", "contact": "Contact et éditeur"},
        "titles": {"index": "Informations légales et assistance", "privacy": "Politique de confidentialité",
                   "delete-account": "Suppression du compte et des données",
                   "contact": "Contact et informations sur l’éditeur"},
        "index": lambda: f"""
<p>{GAME} est un jeu de blocs qui tombent, joué sur un plateau en forme de croix. Chaque branche de la croix est un
monde avec sa propre gravité, et le plateau tourne régulièrement pour vous envoyer dans le monde suivant. Les blocs sont
des verres remplis de liquide dont les couleurs se mélangent.</p>
<p>Éditeur : {PUBLISHER}, France.</p>
<p>Le jeu enregistre le meilleur score, la progression de la campagne et les réglages <strong>uniquement sur
l’appareil</strong>. Il n’a pas de compte propre à l’éditeur, n’affiche aucune publicité et ne propose aucun achat. S’il
est connecté à Google Play Jeux, les réussites et le meilleur score du mode infini sont envoyés à Google (voir la
politique de confidentialité). Ces pages seront mises à jour avant tout changement affectant les données.</p>
""",
        "privacy": lambda: f"""
<h2>Responsable et contact</h2>
<p>Le responsable du traitement est {PUBLISHER}, {ADDRESS}.</p>
<p>Pour toute question relative aux données :
<a href="{mail(GAME + ' - Données personnelles')}">{EMAIL}</a>.</p>

<h2>Données enregistrées par le jeu</h2>
<p>Le jeu conserve uniquement sur l’appareil : le meilleur score, la progression de la campagne (missions réussies et
étoiles obtenues) et les réglages (langue, mode de rotation du plateau, affichage de la pièce fantôme, volume de la
musique et des bruitages). Ces données ne sont jamais transmises à l’éditeur.</p>
<p>Le jeu ne demande ni nom, ni adresse e-mail, ni âge, ni localisation, et n’accède ni aux contacts, ni au micro, ni à
l’appareil photo, ni aux fichiers. Il ne contient ni messagerie ni publicité.</p>

<h2>Google Play Jeux (réussites et classement)</h2>
<p>Au lancement, le jeu tente de se connecter automatiquement à <strong>Google Play Jeux</strong>, le service de Google
qui gère les réussites et les classements. Si vous êtes connecté, le jeu envoie à Google les réussites débloquées et le
meilleur score du mode infini ; Google les associe à votre profil Play Jeux (pseudo et avatar) et affiche le classement
aux autres joueurs selon vos paramètres de visibilité Play Jeux. L’éditeur ne reçoit pas votre adresse e-mail et ne
stocke aucune de ces données sur ses propres serveurs.</p>
<p>Ce traitement est réalisé par Google LLC / Google Ireland Limited selon sa propre
<a href="https://policies.google.com/privacy">politique de confidentialité</a>. Vous pouvez refuser la connexion, gérer
la visibilité de votre profil ou supprimer vos données Play Jeux depuis l’application Google Play Jeux ou les paramètres
de votre compte Google ; le jeu fonctionne entièrement sans connexion.</p>

<h2>Publicité, achats et statistiques</h2>
<p>La version actuelle <strong>n’affiche aucune publicité</strong>, ne propose aucun achat intégré et n’intègre aucun
outil de statistiques ou de suivi. Si l’un de ces éléments est ajouté, cette politique et la section « Sécurité des
données » de Google Play seront mises à jour avant, avec le nom du prestataire et le lien vers sa propre politique.</p>

<h2>Liens externes</h2>
<p>Les liens du jeu vers ces pages s’ouvrent dans votre navigateur. GitHub Pages, qui héberge ces pages, peut
enregistrer des informations techniques (adresse IP, type de navigateur) dans ses journaux de sécurité, selon sa propre
politique de confidentialité.</p>

<h2>Enfants</h2>
<p>{GAME} est un jeu tout public. Il ne collecte pas de données personnelles auprès des enfants. Si vous pensez qu’un
enfant nous a transmis des données (par exemple par e-mail), contactez-nous afin que nous les supprimions.</p>

<h2>Assistance par e-mail</h2>
<p>Lorsque vous contactez l’éditeur, votre adresse e-mail, le contenu de votre message et les éventuelles pièces jointes
sont traités pour répondre à votre demande, traiter un incident ou exercer vos droits. La base juridique est l’intérêt
légitime de l’éditeur à assurer l’assistance.</p>
<p>Ces données sont accessibles à l’éditeur et au fournisseur de messagerie utilisé. Elles sont conservées le temps
nécessaire au traitement, puis au plus trois ans après le dernier échange, sauf obligation légale ou litige.
N’envoyez ni mot de passe ni coordonnées bancaires par e-mail.</p>

<h2>Conservation, suppression et droits</h2>
<p>Les données de jeu restent sur l’appareil jusqu’à ce que vous les effaciez (dans le jeu ou dans les paramètres du
téléphone) ou que vous désinstalliez le jeu : voir <a href="delete-account.html">la page de suppression du compte et des
données</a>. Pour les échanges avec l’assistance, vous pouvez demander l’accès, la rectification, l’effacement, la
limitation, l’opposition ou la portabilité lorsque le droit applicable le prévoit, à l’adresse ci-dessus. Vous pouvez
également introduire une réclamation auprès de la <a href="https://www.cnil.fr/fr/plaintes">CNIL</a>.</p>

<h2>Sécurité</h2>
<p>Le jeu limite ses données à celles décrites ci-dessus. Les messages d’assistance ne
sont accessibles qu’à l’éditeur. Aucun système n’est totalement exempt de risque ; ne transmettez pas de données
sensibles inutiles.</p>

<h2>Modifications</h2>
<p>Cette politique peut évoluer, notamment en cas d’ajout de publicité, d’achats, d’un compte joueur ou d’un mode en
ligne. La date de mise à jour en haut de page sera modifiée et, si le changement est important, il sera signalé dans le
jeu ou sur la fiche Google Play.</p>
""",
        "delete-account": lambda: f"""
<p>Cette page explique comment supprimer les données de <strong>{GAME}</strong>, édité par
<strong>{PUBLISHER}</strong>.</p>

<h2>Compte joueur</h2>
<p>{GAME} <strong>ne crée aucun compte chez l’éditeur</strong> : il n’y a ni identifiant, ni mot de passe, ni profil
stocké sur un serveur de l’éditeur. Il n’y a donc pas de compte à supprimer côté éditeur.</p>
<p>Si vous utilisez <strong>Google Play Jeux</strong>, vos réussites et votre score au classement sont rattachés à votre
profil Play Jeux, géré par Google. Pour les supprimer : application <strong>Google Play Jeux</strong> →
<strong>Paramètres</strong> → supprimer le compte et les données Play Jeux, ou depuis
<a href="https://myaccount.google.com/data-and-privacy">les paramètres de votre compte Google</a>.</p>

<h2>Supprimer les données de jeu</h2>
<p>Le meilleur score, la progression de la campagne et les réglages sont enregistrés uniquement sur l’appareil. Pour les effacer :</p>
<ul>
<li><strong>Dans le jeu :</strong> écran d’accueil → <strong>Paramètres</strong> → <strong>Effacer mes données</strong>,
puis confirmez.</li>
<li><strong>Sur Android :</strong> <strong>Paramètres</strong> du téléphone → <strong>Applications</strong> →
<strong>{GAME}</strong> → <strong>Stockage</strong> → <strong>Effacer les données</strong>.</li>
</ul>
<p>Désinstaller le jeu supprime aussi ces données. Les intitulés peuvent varier selon le téléphone ; pensez également aux
éventuelles sauvegardes automatiques du système (sauvegarde Google).</p>

<h2>Demander la suppression des données détenues par l’éditeur</h2>
<p>Si vous avez écrit à l’assistance, vous pouvez demander la suppression de vos échanges et de votre adresse e-mail :</p>
<p><a class="button" href="{mail(GAME + ' - Suppression de données', 'Bonjour,' + chr(10) + chr(10) + 'Je demande la suppression de mes données liées à ' + GAME + '.' + chr(10) + 'Adresse e-mail utilisée pour contacter l’assistance : ' + chr(10))}">Demander la suppression de mes données</a></p>
<ul>
<li><strong>Données supprimées :</strong> vos messages, pièces jointes et votre adresse e-mail.</li>
<li><strong>Délai :</strong> au plus 30 jours après la réception de votre demande. Une confirmation vous est envoyée.</li>
<li><strong>Conservation éventuelle :</strong> uniquement ce qu’une obligation légale ou un litige en cours impose de
garder, et seulement pendant la durée nécessaire.</li>
</ul>

<h2>Si un compte est ajouté plus tard</h2>
<p>Si une future version ajoute un compte joueur, le jeu proposera la suppression du compte directement dans
l’application, et cette page décrira la procédure, les données supprimées, les délais et les éventuelles conservations.</p>
<p>Plus d’informations : <a href="privacy.html">politique de confidentialité</a>.</p>
""",
        "contact": lambda: f"""
<ul>
<li>Éditeur : {PUBLISHER}.</li>
<li>Adresse : {ADDRESS}.</li>
<li>E-mail : <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
</ul>
<p><a class="button" href="{mail(GAME + ' - Assistance')}">Contacter l’assistance</a></p>
<p>Hébergement des présentes pages : GitHub Pages, fourni par GitHub, Inc., 88 Colin P. Kelly Jr. Street,
San Francisco, CA 94107, États-Unis.</p>
""",
    },

    # ------------------------------------------------------------------ ENGLISH
    "en": {
        "name": "English",
        "date": "October 26, 2026",
        "updated": "Last updated",
        "nav": {"index": "Home", "privacy": "Privacy", "delete-account": "Account and data deletion",
                "contact": "Contact and publisher"},
        "titles": {"index": "Legal information and support", "privacy": "Privacy policy",
                   "delete-account": "Account and data deletion", "contact": "Contact and publisher information"},
        "index": lambda: f"""
<p>{GAME} is a falling-block game played on a cross-shaped board. Each arm of the cross is a world with its own
gravity, and the board turns regularly to send you to the next world. The blocks are glasses filled with liquid whose
colours mix together.</p>
<p>Publisher: {PUBLISHER}, France.</p>
<p>The game stores the best score, campaign progress and settings <strong>on the device only</strong>. It has no
publisher account, shows no ads and offers no purchases. If you are signed in to Google Play Games, achievements and the
endless-mode best score are sent to Google (see the privacy policy). These pages will be updated before any change
affecting data.</p>
""",
        "privacy": lambda: f"""
<h2>Data controller and contact</h2>
<p>The data controller is {PUBLISHER}, {ADDRESS}.</p>
<p>For any question about data: <a href="{mail(GAME + ' - Personal data')}">{EMAIL}</a>.</p>

<h2>Data stored by the game</h2>
<p>The game stores on the device only: the best score, campaign progress (completed missions and stars earned) and the
settings (language, board rotation mode, ghost piece display, music and sound effects volume). This data is never sent
to the publisher.</p>
<p>The game does not ask for your name, email address, age or location, and does not access contacts, microphone,
camera or files. It has no chat and no ads.</p>

<h2>Google Play Games (achievements and leaderboard)</h2>
<p>At launch, the game tries to sign you in automatically to <strong>Google Play Games</strong>, Google’s service for
achievements and leaderboards. If you are signed in, the game sends Google the achievements you unlock and your
endless-mode best score; Google links them to your Play Games profile (gamer name and avatar) and shows the leaderboard
to other players according to your Play Games visibility settings. The publisher does not receive your email address
and stores none of this data on its own servers.</p>
<p>This processing is carried out by Google LLC / Google Ireland Limited under its own
<a href="https://policies.google.com/privacy">privacy policy</a>. You can decline sign-in, manage your profile
visibility or delete your Play Games data from the Google Play Games app or your Google Account settings; the game works
fully without signing in.</p>

<h2>Advertising, purchases and analytics</h2>
<p>The current version <strong>shows no ads</strong>, offers no in-app purchases and includes no analytics or tracking
tool. If any of these is added, this policy and the Google Play “Data safety” section will be updated beforehand, with
the provider’s name and a link to its own policy.</p>

<h2>External links</h2>
<p>Links from the game to these pages open in your browser. GitHub Pages, which hosts these pages, may record technical
information (IP address, browser type) in its security logs, under its own privacy policy.</p>

<h2>Children</h2>
<p>{GAME} is suitable for all ages. It does not collect personal data from children. If you believe a child has sent us
data (for example by email), contact us and we will delete it.</p>

<h2>Email support</h2>
<p>When you contact the publisher, your email address, the content of your message and any attachments are processed to
answer your request, handle an incident or exercise your rights. The legal basis is the publisher’s legitimate interest
in providing support.</p>
<p>This data is accessible to the publisher and to the email provider used. It is kept as long as needed to handle the
request, then at most three years after the last exchange, unless a legal obligation or dispute requires otherwise. Do
not send passwords or bank details by email.</p>

<h2>Retention, deletion and your rights</h2>
<p>Game data stays on the device until you erase it (in the game or in the phone settings) or uninstall the game: see
the <a href="delete-account.html">account and data deletion page</a>. For support exchanges, you can request access,
rectification, erasure, restriction, objection or portability where applicable law provides for it, at the address
above. You can also lodge a complaint with the French data protection authority, the
<a href="https://www.cnil.fr/en/complaints">CNIL</a>, or with your local authority.</p>

<h2>Security</h2>
<p>The game limits its data to what is described above. Support messages are accessible only to
the publisher. No system is completely risk-free; do not send unnecessary sensitive data.</p>

<h2>Changes</h2>
<p>This policy may change, in particular if ads, purchases, a player account or an online mode are added. The date at the
top of the page will be updated and, if the change is significant, it will be announced in the game or on the Google
Play listing.</p>
""",
        "delete-account": lambda: f"""
<p>This page explains how to delete the data of <strong>{GAME}</strong>, published by <strong>{PUBLISHER}</strong>.</p>

<h2>Player account</h2>
<p>{GAME} <strong>does not create any account with the publisher</strong>: there is no username, password or profile
stored on a publisher server. There is therefore no account to delete on the publisher’s side.</p>
<p>If you use <strong>Google Play Games</strong>, your achievements and leaderboard score are linked to your Play Games
profile, managed by Google. To delete them: <strong>Google Play Games</strong> app → <strong>Settings</strong> → delete
your Play Games account and data, or use <a href="https://myaccount.google.com/data-and-privacy">your Google Account
settings</a>.</p>

<h2>Delete game data</h2>
<p>The best score, campaign progress and settings are stored on the device only. To erase them:</p>
<ul>
<li><strong>In the game:</strong> home screen → <strong>Settings</strong> → <strong>Erase my data</strong>, then
confirm.</li>
<li><strong>On Android:</strong> phone <strong>Settings</strong> → <strong>Apps</strong> → <strong>{GAME}</strong> →
<strong>Storage</strong> → <strong>Clear data</strong>.</li>
</ul>
<p>Uninstalling the game also deletes this data. Labels may vary by phone; also consider any automatic system backups
(Google backup).</p>

<h2>Request deletion of data held by the publisher</h2>
<p>If you have written to support, you can request the deletion of your messages and email address:</p>
<p><a class="button" href="{mail(GAME + ' - Data deletion', 'Hello,' + chr(10) + chr(10) + 'I request the deletion of my data related to ' + GAME + '.' + chr(10) + 'Email address used to contact support: ' + chr(10))}">Request deletion of my data</a></p>
<ul>
<li><strong>Data deleted:</strong> your messages, attachments and email address.</li>
<li><strong>Timeframe:</strong> within 30 days of receiving your request. A confirmation is sent to you.</li>
<li><strong>Possible retention:</strong> only what a legal obligation or an ongoing dispute requires us to keep, and only
for as long as necessary.</li>
</ul>

<h2>If an account is added later</h2>
<p>If a future version adds a player account, the game will offer account deletion directly in the app, and this page will
describe the procedure, the data deleted, the timeframes and any retention.</p>
<p>More information: <a href="privacy.html">privacy policy</a>.</p>
""",
        "contact": lambda: f"""
<ul>
<li>Publisher: {PUBLISHER}.</li>
<li>Address: {ADDRESS}.</li>
<li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
</ul>
<p><a class="button" href="{mail(GAME + ' - Support')}">Contact support</a></p>
<p>These pages are hosted by GitHub Pages, provided by GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco,
CA 94107, United States.</p>
""",
    },

    # ------------------------------------------------------------------ ESPAÑOL
    "es": {
        "name": "Español",
        "date": "26 de octubre de 2026",
        "updated": "Última actualización",
        "nav": {"index": "Inicio", "privacy": "Privacidad", "delete-account": "Eliminación de la cuenta y los datos",
                "contact": "Contacto y editor"},
        "titles": {"index": "Información legal y asistencia", "privacy": "Política de privacidad",
                   "delete-account": "Eliminación de la cuenta y los datos",
                   "contact": "Contacto e información del editor"},
        "index": lambda: f"""
<p>{GAME} es un juego de bloques que caen, en un tablero con forma de cruz. Cada brazo de la cruz es un mundo con su
propia gravedad, y el tablero gira con regularidad para enviarte al mundo siguiente. Los bloques son vasos llenos de
líquido cuyos colores se mezclan.</p>
<p>Editor: {PUBLISHER}, Francia.</p>
<p>El juego guarda la mejor puntuación, el progreso de la campaña y los ajustes <strong>solo en el dispositivo</strong>.
No tiene cuenta propia del editor, no muestra publicidad y no ofrece compras. Si has iniciado sesión en Google Play
Juegos, los logros y la mejor puntuación del modo infinito se envían a Google (consulta la política de privacidad).
Estas páginas se actualizarán antes de cualquier cambio que afecte a los datos.</p>
""",
        "privacy": lambda: f"""
<h2>Responsable y contacto</h2>
<p>El responsable del tratamiento es {PUBLISHER}, {ADDRESS}.</p>
<p>Para cualquier pregunta sobre los datos: <a href="{mail(GAME + ' - Datos personales')}">{EMAIL}</a>.</p>

<h2>Datos guardados por el juego</h2>
<p>El juego guarda únicamente en el dispositivo: la mejor puntuación, el progreso de la campaña (misiones superadas y
estrellas obtenidas) y los ajustes (idioma, modo de rotación del tablero, pieza fantasma, volumen de la música y de los
efectos). Estos datos nunca se envían al editor.</p>
<p>El juego no pide nombre, correo electrónico, edad ni ubicación, y no accede a los contactos, al micrófono, a la cámara
ni a los archivos. No tiene chat ni publicidad.</p>

<h2>Google Play Juegos (logros y clasificación)</h2>
<p>Al iniciarse, el juego intenta conectarte automáticamente a <strong>Google Play Juegos</strong>, el servicio de Google
para logros y clasificaciones. Si has iniciado sesión, el juego envía a Google los logros que desbloqueas y tu mejor
puntuación del modo infinito; Google los asocia a tu perfil de Play Juegos (nombre de jugador y avatar) y muestra la
clasificación a otros jugadores según tus ajustes de visibilidad. El editor no recibe tu correo electrónico y no guarda
ninguno de estos datos en sus propios servidores.</p>
<p>Este tratamiento lo realiza Google LLC / Google Ireland Limited según su propia
<a href="https://policies.google.com/privacy">política de privacidad</a>. Puedes rechazar la conexión, gestionar la
visibilidad de tu perfil o eliminar tus datos de Play Juegos desde la aplicación Google Play Juegos o los ajustes de tu
cuenta de Google; el juego funciona por completo sin conexión.</p>

<h2>Publicidad, compras y estadísticas</h2>
<p>La versión actual <strong>no muestra publicidad</strong>, no ofrece compras integradas y no incluye ninguna
herramienta de estadísticas o seguimiento. Si se añade alguno de estos elementos, esta política y la sección
«Seguridad de los datos» de Google Play se actualizarán antes, con el nombre del proveedor y un enlace a su propia
política.</p>

<h2>Enlaces externos</h2>
<p>Los enlaces del juego a estas páginas se abren en tu navegador. GitHub Pages, que aloja estas páginas, puede registrar
información técnica (dirección IP, tipo de navegador) en sus registros de seguridad, según su propia política de
privacidad.</p>

<h2>Menores</h2>
<p>{GAME} es apto para todos los públicos. No recopila datos personales de menores. Si crees que un menor nos ha enviado
datos (por ejemplo por correo electrónico), contáctanos para que los eliminemos.</p>

<h2>Asistencia por correo electrónico</h2>
<p>Cuando contactas con el editor, tu dirección de correo, el contenido de tu mensaje y los posibles archivos adjuntos se
tratan para responder a tu solicitud, resolver una incidencia o ejercer tus derechos. La base jurídica es el interés
legítimo del editor en prestar asistencia.</p>
<p>Estos datos son accesibles para el editor y para el proveedor de correo utilizado. Se conservan el tiempo necesario
para el tratamiento y, como máximo, tres años después del último intercambio, salvo obligación legal o litigio. No
envíes contraseñas ni datos bancarios por correo electrónico.</p>

<h2>Conservación, eliminación y derechos</h2>
<p>Los datos del juego permanecen en el dispositivo hasta que los borres (en el juego o en los ajustes del teléfono) o
desinstales el juego: consulta la <a href="delete-account.html">página de eliminación de la cuenta y los datos</a>. Para
los intercambios con la asistencia, puedes solicitar el acceso, la rectificación, la supresión, la limitación, la
oposición o la portabilidad cuando la ley aplicable lo prevea, en la dirección indicada. También puedes presentar una
reclamación ante la autoridad francesa de protección de datos, la <a href="https://www.cnil.fr/en/complaints">CNIL</a>,
o ante la autoridad de tu país.</p>

<h2>Seguridad</h2>
<p>El juego limita sus datos a los descritos más arriba. Los mensajes de
asistencia solo son accesibles para el editor. Ningún sistema está totalmente libre de riesgos; no envíes datos
sensibles innecesarios.</p>

<h2>Cambios</h2>
<p>Esta política puede cambiar, en particular si se añaden publicidad, compras, una cuenta de jugador o un modo en línea.
La fecha de la parte superior se actualizará y, si el cambio es importante, se anunciará en el juego o en la ficha de
Google Play.</p>
""",
        "delete-account": lambda: f"""
<p>Esta página explica cómo eliminar los datos de <strong>{GAME}</strong>, publicado por <strong>{PUBLISHER}</strong>.</p>

<h2>Cuenta de jugador</h2>
<p>{GAME} <strong>no crea ninguna cuenta con el editor</strong>: no hay identificador, contraseña ni perfil guardado en
un servidor del editor. Por lo tanto, no hay ninguna cuenta que eliminar por parte del editor.</p>
<p>Si usas <strong>Google Play Juegos</strong>, tus logros y tu puntuación en la clasificación están vinculados a tu
perfil de Play Juegos, gestionado por Google. Para eliminarlos: aplicación <strong>Google Play Juegos</strong> →
<strong>Ajustes</strong> → eliminar la cuenta y los datos de Play Juegos, o desde
<a href="https://myaccount.google.com/data-and-privacy">los ajustes de tu cuenta de Google</a>.</p>

<h2>Eliminar los datos del juego</h2>
<p>La mejor puntuación, el progreso de la campaña y los ajustes se guardan únicamente en el dispositivo. Para borrarlos:</p>
<ul>
<li><strong>En el juego:</strong> pantalla de inicio → <strong>Ajustes</strong> → <strong>Borrar mis datos</strong> y
confirma.</li>
<li><strong>En Android:</strong> <strong>Ajustes</strong> del teléfono → <strong>Aplicaciones</strong> →
<strong>{GAME}</strong> → <strong>Almacenamiento</strong> → <strong>Borrar datos</strong>.</li>
</ul>
<p>Desinstalar el juego también elimina estos datos. Los nombres pueden variar según el teléfono; ten en cuenta también
las posibles copias de seguridad automáticas del sistema (copia de seguridad de Google).</p>

<h2>Solicitar la eliminación de los datos que conserva el editor</h2>
<p>Si has escrito a la asistencia, puedes solicitar la eliminación de tus mensajes y de tu dirección de correo:</p>
<p><a class="button" href="{mail(GAME + ' - Eliminación de datos', 'Hola,' + chr(10) + chr(10) + 'Solicito la eliminación de mis datos relacionados con ' + GAME + '.' + chr(10) + 'Dirección de correo utilizada para contactar con la asistencia: ' + chr(10))}">Solicitar la eliminación de mis datos</a></p>
<ul>
<li><strong>Datos eliminados:</strong> tus mensajes, archivos adjuntos y tu dirección de correo.</li>
<li><strong>Plazo:</strong> como máximo 30 días desde la recepción de tu solicitud. Recibirás una confirmación.</li>
<li><strong>Conservación posible:</strong> solo lo que una obligación legal o un litigio en curso obligue a conservar, y
solo durante el tiempo necesario.</li>
</ul>

<h2>Si más adelante se añade una cuenta</h2>
<p>Si una versión futura añade una cuenta de jugador, el juego permitirá eliminarla directamente en la aplicación, y esta
página describirá el procedimiento, los datos eliminados, los plazos y las posibles conservaciones.</p>
<p>Más información: <a href="privacy.html">política de privacidad</a>.</p>
""",
        "contact": lambda: f"""
<ul>
<li>Editor: {PUBLISHER}.</li>
<li>Dirección: {ADDRESS}.</li>
<li>Correo electrónico: <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
</ul>
<p><a class="button" href="{mail(GAME + ' - Asistencia')}">Contactar con la asistencia</a></p>
<p>Alojamiento de estas páginas: GitHub Pages, proporcionado por GitHub, Inc., 88 Colin P. Kelly Jr. Street,
San Francisco, CA 94107, Estados Unidos.</p>
""",
    },

    # ------------------------------------------------------------------ ITALIANO
    "it": {
        "name": "Italiano",
        "date": "26 ottobre 2026",
        "updated": "Ultimo aggiornamento",
        "nav": {"index": "Home", "privacy": "Privacy", "delete-account": "Eliminazione dell’account e dei dati",
                "contact": "Contatti ed editore"},
        "titles": {"index": "Informazioni legali e assistenza", "privacy": "Informativa sulla privacy",
                   "delete-account": "Eliminazione dell’account e dei dati",
                   "contact": "Contatti e informazioni sull’editore"},
        "index": lambda: f"""
<p>{GAME} è un gioco di blocchi che cadono, su un tabellone a forma di croce. Ogni braccio della croce è un mondo con la
propria gravità, e il tabellone ruota regolarmente per mandarti nel mondo successivo. I blocchi sono bicchieri pieni di
liquido i cui colori si mescolano.</p>
<p>Editore: {PUBLISHER}, Francia.</p>
<p>Il gioco salva il punteggio migliore, i progressi della campagna e le impostazioni <strong>solo sul
dispositivo</strong>. Non ha un account proprio dell’editore, non mostra pubblicità e non offre acquisti. Se hai
effettuato l’accesso a Google Play Giochi, gli obiettivi e il punteggio migliore della modalità infinita vengono inviati
a Google (vedi l’informativa sulla privacy). Queste pagine saranno aggiornate prima di qualsiasi modifica che riguardi i
dati.</p>
""",
        "privacy": lambda: f"""
<h2>Titolare e contatti</h2>
<p>Il titolare del trattamento è {PUBLISHER}, {ADDRESS}.</p>
<p>Per qualsiasi domanda sui dati: <a href="{mail(GAME + ' - Dati personali')}">{EMAIL}</a>.</p>

<h2>Dati salvati dal gioco</h2>
<p>Il gioco salva esclusivamente sul dispositivo: il punteggio migliore, i progressi della campagna (missioni completate
e stelle ottenute) e le impostazioni (lingua, modalità di rotazione del tabellone, pezzo fantasma, volume della musica e
degli effetti). Questi dati non vengono mai inviati all’editore.</p>
<p>Il gioco non chiede nome, indirizzo e-mail, età o posizione, e non accede a contatti, microfono, fotocamera o file.
Non ha chat né pubblicità.</p>

<h2>Google Play Giochi (obiettivi e classifica)</h2>
<p>All’avvio, il gioco prova a collegarti automaticamente a <strong>Google Play Giochi</strong>, il servizio di Google
per obiettivi e classifiche. Se hai effettuato l’accesso, il gioco invia a Google gli obiettivi sbloccati e il punteggio
migliore della modalità infinita; Google li associa al tuo profilo Play Giochi (nome giocatore e avatar) e mostra la
classifica agli altri giocatori secondo le tue impostazioni di visibilità. L’editore non riceve il tuo indirizzo e-mail
e non conserva nessuno di questi dati sui propri server.</p>
<p>Questo trattamento è effettuato da Google LLC / Google Ireland Limited secondo la propria
<a href="https://policies.google.com/privacy">informativa sulla privacy</a>. Puoi rifiutare l’accesso, gestire la
visibilità del profilo o eliminare i tuoi dati Play Giochi dall’app Google Play Giochi o dalle impostazioni del tuo
account Google; il gioco funziona completamente anche senza accesso.</p>

<h2>Pubblicità, acquisti e statistiche</h2>
<p>La versione attuale <strong>non mostra pubblicità</strong>, non offre acquisti in-app e non include strumenti di
statistica o tracciamento. Se uno di questi elementi verrà aggiunto, questa informativa e la sezione «Sicurezza dei
dati» di Google Play saranno aggiornate prima, con il nome del fornitore e un link alla sua informativa.</p>

<h2>Link esterni</h2>
<p>I link del gioco verso queste pagine si aprono nel tuo browser. GitHub Pages, che ospita queste pagine, può registrare
informazioni tecniche (indirizzo IP, tipo di browser) nei propri log di sicurezza, secondo la propria informativa sulla
privacy.</p>

<h2>Minori</h2>
<p>{GAME} è adatto a tutte le età. Non raccoglie dati personali dai minori. Se ritieni che un minore ci abbia inviato
dati (ad esempio via e-mail), contattaci e li elimineremo.</p>

<h2>Assistenza via e-mail</h2>
<p>Quando contatti l’editore, il tuo indirizzo e-mail, il contenuto del messaggio e gli eventuali allegati sono trattati
per rispondere alla richiesta, gestire un problema o esercitare i tuoi diritti. La base giuridica è il legittimo
interesse dell’editore a fornire assistenza.</p>
<p>Questi dati sono accessibili all’editore e al fornitore di posta utilizzato. Sono conservati per il tempo necessario
alla gestione e al massimo tre anni dopo l’ultimo scambio, salvo obblighi di legge o controversie. Non inviare password
né dati bancari via e-mail.</p>

<h2>Conservazione, cancellazione e diritti</h2>
<p>I dati di gioco restano sul dispositivo finché non li cancelli (nel gioco o nelle impostazioni del telefono) o non
disinstalli il gioco: vedi la <a href="delete-account.html">pagina di eliminazione dell’account e dei dati</a>. Per gli
scambi con l’assistenza, puoi chiedere accesso, rettifica, cancellazione, limitazione, opposizione o portabilità quando
la legge applicabile lo prevede, all’indirizzo sopra. Puoi anche presentare un reclamo all’autorità francese per la
protezione dei dati, la <a href="https://www.cnil.fr/en/complaints">CNIL</a>, o all’autorità del tuo paese (in Italia,
il Garante per la protezione dei dati personali).</p>

<h2>Sicurezza</h2>
<p>Il gioco limita i propri dati a quelli descritti sopra. I messaggi di
assistenza sono accessibili solo all’editore. Nessun sistema è totalmente privo di rischi; non inviare dati sensibili non
necessari.</p>

<h2>Modifiche</h2>
<p>Questa informativa può cambiare, in particolare in caso di aggiunta di pubblicità, acquisti, un account giocatore o una
modalità online. La data in alto sarà aggiornata e, se la modifica è importante, sarà segnalata nel gioco o nella scheda
Google Play.</p>
""",
        "delete-account": lambda: f"""
<p>Questa pagina spiega come eliminare i dati di <strong>{GAME}</strong>, pubblicato da <strong>{PUBLISHER}</strong>.</p>

<h2>Account giocatore</h2>
<p>{GAME} <strong>non crea alcun account presso l’editore</strong>: non ci sono nome utente, password o profilo salvati
su un server dell’editore. Non c’è quindi alcun account da eliminare presso l’editore.</p>
<p>Se usi <strong>Google Play Giochi</strong>, i tuoi obiettivi e il punteggio in classifica sono collegati al tuo
profilo Play Giochi, gestito da Google. Per eliminarli: app <strong>Google Play Giochi</strong> →
<strong>Impostazioni</strong> → elimina l’account e i dati Play Giochi, oppure dalle
<a href="https://myaccount.google.com/data-and-privacy">impostazioni del tuo account Google</a>.</p>

<h2>Eliminare i dati di gioco</h2>
<p>Il punteggio migliore, i progressi della campagna e le impostazioni sono salvati solo sul dispositivo. Per cancellarli:</p>
<ul>
<li><strong>Nel gioco:</strong> schermata iniziale → <strong>Impostazioni</strong> → <strong>Cancella i miei
dati</strong>, poi conferma.</li>
<li><strong>Su Android:</strong> <strong>Impostazioni</strong> del telefono → <strong>App</strong> →
<strong>{GAME}</strong> → <strong>Spazio di archiviazione</strong> → <strong>Cancella dati</strong>.</li>
</ul>
<p>Anche la disinstallazione del gioco elimina questi dati. Le voci possono variare a seconda del telefono; considera anche
gli eventuali backup automatici del sistema (backup di Google).</p>

<h2>Richiedere l’eliminazione dei dati conservati dall’editore</h2>
<p>Se hai scritto all’assistenza, puoi chiedere l’eliminazione dei tuoi messaggi e del tuo indirizzo e-mail:</p>
<p><a class="button" href="{mail(GAME + ' - Eliminazione dei dati', 'Buongiorno,' + chr(10) + chr(10) + 'Chiedo l’eliminazione dei miei dati relativi a ' + GAME + '.' + chr(10) + 'Indirizzo e-mail usato per contattare l’assistenza: ' + chr(10))}">Richiedi l’eliminazione dei miei dati</a></p>
<ul>
<li><strong>Dati eliminati:</strong> i tuoi messaggi, gli allegati e il tuo indirizzo e-mail.</li>
<li><strong>Tempi:</strong> entro 30 giorni dal ricevimento della richiesta. Ti verrà inviata una conferma.</li>
<li><strong>Eventuale conservazione:</strong> solo ciò che un obbligo di legge o una controversia in corso impone di
conservare, e solo per il tempo necessario.</li>
</ul>

<h2>Se in futuro verrà aggiunto un account</h2>
<p>Se una versione futura aggiungerà un account giocatore, il gioco ne permetterà l’eliminazione direttamente nell’app, e
questa pagina descriverà la procedura, i dati eliminati, i tempi e le eventuali conservazioni.</p>
<p>Maggiori informazioni: <a href="privacy.html">informativa sulla privacy</a>.</p>
""",
        "contact": lambda: f"""
<ul>
<li>Editore: {PUBLISHER}.</li>
<li>Indirizzo: {ADDRESS}.</li>
<li>E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
</ul>
<p><a class="button" href="{mail(GAME + ' - Assistenza')}">Contatta l’assistenza</a></p>
<p>Hosting di queste pagine: GitHub Pages, fornito da GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco,
CA 94107, Stati Uniti.</p>
""",
    },
}

DEFAULT_LANG = "en"


def lang_switcher(current, page):
    items = []
    for code, L in LANGS.items():
        cls = ' class="current" aria-current="true"' if code == current else ""
        items.append(f'<a href="../{code}/{page}.html" hreflang="{code}" lang="{code}"{cls}>{code.upper()}</a>')
    return '<nav class="langs" aria-label="Language">' + "".join(items) + "</nav>"


def page_html(code, page):
    L = LANGS[code]
    title = L["titles"][page]
    nav = " · ".join(
        f'<a href="{p}.html"{" aria-current=\"page\"" if p == page else ""}>{html.escape(L["nav"][p])}</a>' for p in PAGES)
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{c}" href="{BASE_URL}{c}/{page}.html">' for c in LANGS)
    links = ""
    if page == "index":
        links = "<ul class=\"cards\">" + "".join(
            f'<li><a href="{p}.html">{html.escape(L["nav"][p])}</a></li>' for p in PAGES if p != "index") + "</ul>"
    return f"""<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — {GAME}</title>
<meta name="description" content="{html.escape(GAME + ' — ' + title)}">
<link rel="icon" type="image/png" href="../assets/icon.png">
<link rel="apple-touch-icon" href="../assets/icon.png">
<link rel="stylesheet" href="../assets/style.css">
{alternates}
</head>
<body>
<header class="hero">
  {lang_switcher(code, page)}
  <a class="brand" href="index.html"><img src="../assets/icon.png" alt="" width="64" height="64"><span>{GAME}</span></a>
  <h1>{html.escape(title)}</h1>
  <p class="date">{L["updated"]}{" :" if code == "fr" else ":"} {L["date"]}</p>
</header>
<main>
{L[page]()}
{links}
</main>
<footer><nav>{nav}</nav></footer>
</body>
</html>
"""


def redirect_html(page):
    """Page racine : envoie vers la langue du navigateur, avec des liens si le script est bloqué."""
    codes = list(LANGS)
    links = "".join(
        f'<li><a href="{c}/{page}.html" hreflang="{c}" lang="{c}">{LANGS[c]["name"]} — '
        f'{html.escape(LANGS[c]["titles"][page] if page != "index" else LANGS[c]["titles"]["index"])}</a></li>'
        for c in codes)
    return f"""<!doctype html>
<html lang="{DEFAULT_LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{GAME}</title>
<link rel="icon" type="image/png" href="assets/icon.png">
<link rel="stylesheet" href="assets/style.css">
<script>
(function () {{
  var supported = {codes!r};
  var prefs = navigator.languages || [navigator.language || "{DEFAULT_LANG}"];
  var lang = "{DEFAULT_LANG}";
  for (var i = 0; i < prefs.length; i++) {{
    var c = String(prefs[i]).slice(0, 2).toLowerCase();
    if (supported.indexOf(c) >= 0) {{ lang = c; break; }}
  }}
  location.replace(lang + "/{page}.html");
}})();
</script>
</head>
<body>
<header class="hero">
  <a class="brand" href="index.html"><img src="assets/icon.png" alt="" width="64" height="64"><span>{GAME}</span></a>
  <h1>Choose your language</h1>
</header>
<main><ul class="cards">{links}</ul></main>
</body>
</html>
"""


CSS = """
:root { --bg: #0f0f1c; --panel: #1a1a2e; --text: #e8eaf6; --muted: #a9aed0; --accent: #ffd933; --link: #8fb8ff; }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--text);
       font: 17px/1.6 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }
.hero { background: linear-gradient(135deg, #1a1634, #3a185c); padding: 20px 16px 28px; text-align: center; }
.brand { display: inline-flex; align-items: center; gap: 12px; color: #fff; text-decoration: none;
         font-weight: 800; font-size: 1.5rem; margin-top: 8px; }
.brand img { border-radius: 14px; box-shadow: 0 6px 18px rgba(0,0,0,.4); }
h1 { margin: 16px 0 4px; font-size: 1.6rem; line-height: 1.25; }
.date { margin: 0; color: var(--muted); font-size: .95rem; }
.langs { display: flex; justify-content: flex-end; gap: 6px; flex-wrap: wrap; }
.langs a { color: var(--muted); text-decoration: none; padding: 2px 8px; border-radius: 8px;
           border: 1px solid rgba(255,255,255,.15); font-size: .85rem; font-weight: 700; }
.langs a.current { color: #1a1634; background: var(--accent); border-color: var(--accent); }
main { max-width: 760px; margin: 0 auto; padding: 8px 16px 32px; }
h2 { margin-top: 2rem; font-size: 1.2rem; color: var(--accent); }
a { color: var(--link); }
.button { display: inline-block; background: var(--accent); color: #1a1634; font-weight: 700;
          padding: 10px 18px; border-radius: 12px; text-decoration: none; }
.cards { list-style: none; padding: 0; display: grid; gap: 10px; margin-top: 1.5rem; }
.cards a { display: block; background: var(--panel); padding: 14px 18px; border-radius: 12px;
           text-decoration: none; color: var(--text); font-weight: 600; border: 1px solid rgba(255,255,255,.08); }
.cards a:hover { border-color: var(--accent); }
footer { border-top: 1px solid rgba(255,255,255,.08); padding: 16px; text-align: center; font-size: .9rem; }
footer a { color: var(--muted); }
footer a[aria-current] { color: var(--text); font-weight: 700; }
"""


def main():
    os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
    with open(os.path.join(HERE, "assets", "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS.lstrip())
    icon_src = os.path.join(HERE, "..", "PlayStore", "icone_512.png")
    if os.path.exists(icon_src):
        shutil.copyfile(icon_src, os.path.join(HERE, "assets", "icon.png"))

    for code in LANGS:
        os.makedirs(os.path.join(HERE, code), exist_ok=True)
        for page in PAGES:
            with open(os.path.join(HERE, code, page + ".html"), "w", encoding="utf-8") as f:
                f.write(page_html(code, page))

    for page in PAGES:
        with open(os.path.join(HERE, page + ".html"), "w", encoding="utf-8") as f:
            f.write(redirect_html(page))

    open(os.path.join(HERE, ".nojekyll"), "w").close()
    print("Site généré :", ", ".join(LANGS))


if __name__ == "__main__":
    main()
