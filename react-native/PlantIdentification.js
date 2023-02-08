import { View, Text, SafeAreaView, ScrollView, StyleSheet, TouchableOpacity, Image} from 'react-native';
import React, { useState } from 'react';
import FontAwesome5Icon from 'react-native-vector-icons/FontAwesome5';
import * as ImagePicker from 'expo-image-picker';

const PlantIdentification = () => {
    const apiKey = 'Your api key';
    const [plantImage, setPlantImage] = useState(null);
    const [plantImageUri, setPlantImageUri] = useState(null);
    const [plantDetails, setPlantDetails] = useState([]);

    const pickImageCamera = async () => {
        const permissionResult = await ImagePicker.requestCameraPermissionsAsync();
        if (permissionResult.granted === false) {
            alert("You've refused to allow this appp to access your camera!");
            return;
        }

        const result = await ImagePicker.launchCameraAsync({
            allowsEditing: true,
            aspect: [4, 3],
            quality: 1,
            base64: true
        });
        
        if (!result.cancelled) {
            setPlantImageUri(result.uri);
            setPlantImage(result);
        }
    };

    const pickImageLibrary = async () => {
        const permissionResult = await ImagePicker.requestMediaLibraryPermissionsAsync();
        if (permissionResult.granted === false) {
            alert("You've refused to allow this appp to access your photos!");
            return;
        }

        const result = await ImagePicker.launchImageLibraryAsync({
            mediaTypes: ImagePicker.MediaTypeOptions.All,
            allowsEditing: true,
            aspect: [4, 3],
            quality: 1,
            base64: true
        });
        
        if (!result.cancelled) {
            setPlantImageUri(result.uri)
            setPlantImage(result);
        }
    };
    
    const launchImagePicker = async () => {
        if(!plantImage){
            return;
        }
        const base64Image = ['data:image/jpeg;base64,' + plantImage.base64];

        fetch('https://api.plant.id/v2/identify', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                api_key: apiKey,
                images: base64Image,
            })
            })
            .then((response) => {
                return response.json();
            })
            .then((responseJson) => {
                setPlantDetails(responseJson.suggestions);
            })
            .catch((error) => {
                console.error(error);
            });
      };
        
    return (
    <SafeAreaView style={{ backgroundColor: "#F2FFF2", flex: 1 }}>
        <ScrollView showsVerticalScrollIndicator={false} >
        <View style={styles.buttonContainer}>
            <TouchableOpacity onPress={pickImageCamera}>
              <FontAwesome5Icon
                name={"camera"} 
                size={20} 
                style={{
                  marginBottom: 3,
                  alignSelf: "center",
                  color: "#325232"
                }} 
              />
              <Text style={styles.iconText}>Kamera</Text>
            </TouchableOpacity>
            <TouchableOpacity onPress={pickImageLibrary}>
              <FontAwesome5Icon
                name={"image"} 
                size={20} 
                style={{
                  marginBottom: 3,
                  alignSelf: "center",
                  color: "#325232"
                }} 
              />
              <Text style={styles.iconText}>Gallerie</Text>
            </TouchableOpacity>
        </View>
        <View style={styles.imageContainer}>
          {
            plantImageUri !== '' && <Image
              source={{ uri: plantImageUri }}
              style={styles.image}
            /> 
          }
        </View>
        {plantImage && (
        <>
            <TouchableOpacity
                style={styles.saveButton}
                onPress={() => launchImagePicker()}
            >
                <Text style={styles.saveText}>Identify Plant</Text>
            </TouchableOpacity>
            {plantDetails && (
                plantDetails.map((value, index) => {
                    return <View key={index}>
                        <Text>Scientific name: {value.plant_details.scientific_name}</Text>
                        <Text>Probability: {value.plant_details.probability.round(2) * 100 + '%'}</Text>
                        <Text>Wiki description: {value.plant_details.wiki_description}</Text>
                    </View>
                })
            )}
        </>
        )}
        </ScrollView> 
    </SafeAreaView>
  )
}

export default PlantIdentification

const styles = StyleSheet.create({
    saveButton:{
        backgroundColor: "#325232",
        borderRadius: 30,
        width: "50%",
        marginLeft: 30,
        padding:10
    },
    saveText:{
        color:"#B2D0B2",
        fontWeight: "700",
        textAlign: "center"
    },
    container: {
      margin: 10,
      marginLeft: 25,
      paddingHorizontal: 15,
      paddingVertical: 13,
      justifyContent: "space-evenly",
      alignItems: "center",
      flexDirection: "row",
      width: "87%",
      backgroundColor: "#B2D0B2",
      borderRadius: 15,
    },
    buttonContainer:{
      flexDirection: "row", 
      marginVertical: 10,
      marginHorizontal: 25,
      justifyContent: "space-around",
      backgroundColor: "#b2d0B2",
      borderRadius: 30,
      padding: 10,
      width: "50%"
    },
    iconText: {
      fontSize: 12
    },
    imageContainer: {
      paddingLeft: 30,
      paddingVertical: 15
    },
    image: {
      width: 100,
      height: 100,
      resizeMode: 'cover'
    },
});