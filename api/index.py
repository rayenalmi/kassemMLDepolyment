from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
 #bech ywalii https 5ater pwa
#import ssl
#context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#context.load_cert_chain('cert.pem', 'key.pem')

app = Flask(__name__,static_url_path='/static')
#context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
#context.load_cert_chain('cert.pem', 'key.pem')

# Load your training data
data_train_with_features_selected = pd.read_csv('data_train_top_10_features.csv')  # Update with your actual path

# Assuming you already have data_train_with_features_selected
# Load your training data
data_train_with_features_selected = pd.read_csv('data_train_top_10_features.csv')  # Update with your actual path

# Split the data into features (X) and target variable (y)
X = data_train_with_features_selected.drop('attack', axis=1)
y = data_train_with_features_selected['attack']

# Split the data into training and testing sets (e.g., 80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert data to NumPy arrays
X_train_np, y_train_np = X_train.to_numpy(), y_train.to_numpy()
X_test_np, y_test_np = X_test.to_numpy(), y_test.to_numpy()

# Create and train the KNN classifier
knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_classifier.fit(X_train_np, y_train_np)

# Make predictions on the test set
y_pred = knn_classifier.predict(X_test_np)

# Calculate accuracy
accuracy = accuracy_score(y_test_np, y_pred)

# Display the accuracy
print(f"Accuracy on the test set: {accuracy:.2%}")

# Define the min-max scaling function
'''def min_max_scaling(df):
    df_norm = df.copy()
    for column in df_norm.columns:
        if df_norm[column].dtype in ['int64', 'float64']:
            if df_norm[column].max() - df_norm[column].min() != 0:
                df_norm[column] = (df_norm[column] - df_norm[column].min()) / (df_norm[column].max() - df_norm[column].min())
            else:
                df_norm[column] = 0.0

    return df_norm'''

#vizualize data_train
@app.route('/visualize', methods=['GET', 'POST'])
def visualize():
        # Charger le dataset train
    train_data = pd.read_csv('data_train.csv')

    # Nombre de lignes à afficher par page
    rows_per_page = 10

    # Obtenir le numéro de page à partir de l'argument de requête
    page = request.args.get('page', 1, type=int)

    # Sélectionner les lignes à afficher pour le train
    train_subset = train_data.iloc[(page - 1) * rows_per_page: page * rows_per_page]

    # Convertir les DataFrames en format HTML pour l'affichage
    train_html = train_subset.to_html()
    columns = train_data.columns.tolist()
    data = train_data.to_dict(orient='records')
    return render_template('tables.html',columns=columns, data=data,train_html=train_html,page=page,rows_per_page=rows_per_page,train_data=train_data)

###############################################################################################################################################################

#vizualize data_test
@app.route('/visualizeTest', methods=['GET', 'POST'])
def visualizeTest():
        # Charger le dataset train
    train_data = pd.read_csv('data_test.csv')

    # Nombre de lignes à afficher par page
    rows_per_page = 10

    # Obtenir le numéro de page à partir de l'argument de requête
    page = request.args.get('page', 1, type=int)

    # Sélectionner les lignes à afficher pour le train
    train_subset = train_data.iloc[(page - 1) * rows_per_page: page * rows_per_page]

    # Convertir les DataFrames en format HTML pour l'affichage
    train_html = train_subset.to_html()
    columns = train_data.columns.tolist()
    data = train_data.to_dict(orient='records')
    return render_template('tablesTest.html',columns=columns, data=data,train_html=train_html,page=page,rows_per_page=rows_per_page,train_data=train_data)
###############################################################################################################################################################
@app.route('/KNNModel', methods=['GET', 'POST'])
def KNNModel():
    # Charger le dataset train
    train_data = pd.read_csv('data_train_top_10_features.csv')
    predicted_attack = None
    data = pd.read_csv('data_test.csv')

    #DOS BEGING COUNT NUMBER OF OCCURENCE OF EACH TYPE ATTACK OF DOS
    attack_types = [
    "neptune", "back", "land", "pod", "smurf",
    "teardrop", "mailbomb", "apache2", "processtable", "udpstorm", "worm"
    ]
    attack_counts1 = {attack_type: 0 for attack_type in attack_types}
    for attack_type in attack_types:
        count = data[data['attack'] == attack_type].shape[0]
        attack_counts1[attack_type] = count
        #print(f"{attack_type}: {count} occurrences")
    attack_counts_list = list(attack_counts1.values())
    #print("Attack Counts List:", attack_counts_list)
    #print(attack_types)
    #EndDOS BEGING COUNT NUMBER OF OCCURENCE OF EACH TYPE ATTACK OF DOS

    #U2R BEGING COUNT NUMBER OF OCCURENCE OF EACH TYPE ATTACK OF U2R
    attack_types1 = [
    "buffer_overflow", "loadmodule", "perl", "rootkit", "ps","sqlattack", "xterm"]
    attack_counts_U2R = {attack_type: 0 for attack_type in attack_types1}
    for attack_type in attack_types1:
        count = data[data['attack'] == attack_type].shape[0]
        attack_counts_U2R[attack_type] = count
        #print(f"{attack_type}: {count} occurrences")
    attack_counts_U2R_list = list(attack_counts_U2R.values())
    #print("Attack Counts List:", attack_counts_U2R_list)
    #print(attack_types1)
    #END U2R BEGING COUNT NUMBER OF OCCURENCE OF EACH TYPE ATTACK OF U2R

    #BEGIN Probe BEGING COUNT NUMBER OF OCCURENCE OF EACH TYPE ATTACK OF Probe
    attack_types2 = [
    "ipsweep", "nmap", "portsweep", "satan", "mscan","saint"
    ]
    attack_counts_Probe = {attack_type: 0 for attack_type in attack_types2}
    for attack_type in attack_types2:
        count = data[data['attack'] == attack_type].shape[0]
        attack_counts_Probe[attack_type] = count
        #print(f"{attack_type}: {count} occurrences")
    attack_counts_Probe_list = list(attack_counts_Probe.values())
    #print("Attack Counts List2:", attack_counts_Probe_list)
    #print(attack_types2)

    #END Probe BEGING COUNT NUMBER OF OCCURENCE OF EACH TYPE ATTACK OF Probe

    #BEGIN R2L BEGING COUNT NUMBER OF OCCURENCE OF EACH TYPE ATTACK OF R2L
    attack_types3 = [
    "ftp_write", "guess_passwd", "imap", "multihop", "phf", "spy", "warezclient", "warezmaster", "sendmail", "named", "snmpgetattack", "snmpguess", "xlock", "xsnoop", "httptunnel"
    ]
    attack_counts_R2L = {attack_type: 0 for attack_type in attack_types3}
    for attack_type in attack_types3:
        count = data[data['attack'] == attack_type].shape[0]
        attack_counts_R2L[attack_type] = count
        #print(f"{attack_type}: {count} occurrences")
    attack_counts_R2L_list = list(attack_counts_R2L.values())
    print("Attack Counts List3:", attack_counts_R2L_list)
    print(attack_types3)
    #END R2L BEGING COUNT NUMBER OF OCCURENCE OF EACH TYPE ATTACK OF R2L

    #Normal BEGING COUNT NUMBER OF OCCURENCE OF EACH TYPE ATTACK OF normal
    #END BEGING COUNT NUMBER OF OCCURENCE OF EACH TYPE ATTACK OF normal

    if request.method == 'POST':
        try:
            ###############################################################
            # Récupérer les données du formulaire pour les features
            feature_values = [float(request.form[f'feature{i}']) for i in range(1, 11)]
            # Créer un DataFrame avec les données d'entrée
            input_data = pd.DataFrame(data=[feature_values], columns=list(X_train.columns))
            # Faire des prédictions sur les données d'entrée
            numerical_prediction = knn_classifier.predict(input_data)[0]
            # Convertir la prédiction numérique en un format lisible par l'homme
            attack_mapping = {0: 'Normal', 1: 'DoS', 2: 'U2R', 3: 'R2L', 4: 'Probe'}
            predicted_attack = attack_mapping.get(numerical_prediction, 'Unknown')

            # Rediriger vers une page spécifique en fonction du type d'attaque prédit
            if predicted_attack == 'Normal':
                return render_template('normal_page.html', predicted_attack=predicted_attack)
            elif predicted_attack == 'DoS':
                return render_template('dos_page.html', predicted_attack=predicted_attack,attack_types=attack_types,attack_counts_list=attack_counts_list)
            elif predicted_attack == 'U2R':
                return render_template('u2r_page.html', predicted_attack=predicted_attack,attack_types1=attack_types1,attack_counts_U2R_list=attack_counts_U2R_list)
            elif predicted_attack == 'R2L':
                return render_template('r2l_page.html', predicted_attack=predicted_attack)
            elif predicted_attack == 'Probe':
                return render_template('probe_page.html', predicted_attack=predicted_attack,attack_types2=attack_types2,attack_counts_Probe_list=attack_counts_Probe_list)
            else:
                return render_template('404.html', predicted_attack=predicted_attack)

        except ValueError as e:
            # Gérer une entrée invalide (valeurs non numériques, etc.)
            print(f"Error: {e}")
            predicted_attack = "Invalid input"

    return render_template('knn.html', predicted_attack=predicted_attack)

###############################################################################################################################################################


###############################################################################################################################################################
@app.route('/', methods=['GET', 'POST'])
def index():
    train_data10 = pd.read_csv('dataWithNameAttack.csv')
    train_data = pd.read_csv('data_train.csv')
    # Calculer les données du graphique
    attack_counts = train_data['attack'].value_counts()
    attack_types = attack_counts.index.tolist()
    counts = attack_counts.tolist()
    #print(counts)
    ###############
    # Compter les occurrences pour chaque valeur de 'protocol_type'
    protocol_type_counts = train_data['protocol_type'].value_counts()
    protocol_type_types = protocol_type_counts.index.tolist()
    counts_protocol_type = protocol_type_counts.tolist()
    #print(counts_protocol_type)
    ###############
    protocol_attack_counts = train_data.groupby(['protocol_type', 'attack']).size().unstack().fillna(0)
    print(protocol_attack_counts)
    protocol_types = protocol_attack_counts.index.tolist()
    attack_types1 = protocol_attack_counts.columns.tolist()
    counts_by_protocol = protocol_attack_counts.values.tolist()
    ##############
    # Afficher pour chaque service ne nombre d'attack
    service_counts = train_data['service'].value_counts()
    service_types = service_counts.index.tolist()
    counts_service = service_counts.tolist()
    ###############
    attack_counts2 = train_data10['attack'].value_counts()
    attack_types2 = attack_counts2.index.tolist()
    counts2 = attack_counts2.tolist()
    ################
    duration_data = train_data['duration'].tolist()
    #print(duration_data)
    return render_template('/index.html',accuracy=accuracy,duration_data=duration_data,attack_types2=attack_types2,counts2=counts2,service_types=service_types, counts_service=counts_service,protocol_types=protocol_types,attack_types1=attack_types1,counts_by_protocol=counts_by_protocol, attack_types=attack_types, counts=counts,protocol_type_types=protocol_type_types, counts_protocol_type=counts_protocol_type)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

