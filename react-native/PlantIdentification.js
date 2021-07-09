import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  Image,
  FlatList,
  Dimensions,
  Button,
  ActivityIndicator,
} from 'react-native';
import ImagePicker from 'react-native-image-picker';

export default function PlantIdentification() {
  const [avatarSource, setAvatarSource] = useState('');
  const [error, setError] = useState('');
  const [speciesFound, setSpeciesFound] = useState(false);
  const [plantIDData, setPlantIDData] = useState({});
  const [loading, setLoading] = useState(false);

  // ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
  //YOUR PLANT ID API KEY:
  const apiKey = 'xxx';
  // ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––


  const options = {
    title: 'Select plant picture',
    storageOptions: {
      skipBackup: true,
      path: 'images',
    },
  };

  const launchImagePicker = () => {
    ImagePicker.showImagePicker(options, (response) => {
      if (response.didCancel) {
        console.log('User cancelled image picker');
      } else if (response.error) {
        setError(response.error);
      } else {
        const source = 'data:image/jpeg;base64,' + response.data;
        const base64Image = ['data:image/jpeg;base64,' + response.data];
        const data = {
          api_key: apiKey,
          images: base64Image,
          modifiers: ['crops_fast', 'similar_images'],
          plant_language: 'en',
          plant_details: [
            'common_names',
            'url',
            'name_authority',
            'wiki_description',
            'taxonomy',
            'synonyms',
          ],
        };
        setLoading(true);
        fetch('https://api.plant.id/v2/identify', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        })
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            setPlantIDData(data);
            setSpeciesFound(true);
          })
          .catch((error) => {
            setError(error);
            setLoading(false);
          });
        setAvatarSource(source);
        setLoading(false);
      }
    });
  };

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#1F9664" />
      </View>
    );
  } else if (!speciesFound) {
    return (
      <View style={styles.container}>
        <Text>Start by taking a picture of your plant.</Text>
        <Text>{error}</Text>
        <Button
          title="Add a picture"
          onPress={() => {
            launchImagePicker();
          }}
        />
      </View>
    );
  } else {
    return (
      <View style={styles.container}>
        <Text style={styles.subTitle}>My picture:</Text>
        <Image style={styles.image} source={{ uri: avatarSource }} />

        <Text style={styles.error}>{error}</Text>
        <Text style={styles.subTitle}>
          Results from Plant.id:
        </Text>
        <FlatList
          data={plantIDData.suggestions}
          renderItem={({ item, index }) => (
            <View
              style={styles.mainEntry}>
              <Image
                style={styles.mainEntryImage}
                source={{
                  uri:
                    item.similar_images.length <= 0
                      ? 'https://plant.id/assets/home/plants.png'
                      : item.similar_images[0].url,
                }}></Image>
              <View>
                <Text style={styles.cardTitle}>
                  {item.plant_details.scientific_name}
                </Text>
                <Text>
                  Probability: {item.probability.toFixed(2) * 100 + '%'}
                </Text>
                <Text>{item.plant_details.taxonomy.kingdom}</Text>
              </View>
            </View>
          )}
          keyExtractor={(item, index) => index.toString()}
        />
      </View>
    );
  }
}
const styles = StyleSheet.create({
  container: {
    backgroundColor: '#f5f5f1',
    padding: 32,
  },
  cardTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: 'black',
  },
  subTitle: {
    fontSize: 24,
    marginBottom: 32
  },
  error: {
    fontSize: 18,
    color: 'red',
  },
  image: {
    width: 100,
    height: 100,
    borderRadius: 12,
  },
  loadingContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  mainEntry: {
    backgroundColor: 'white',
    padding: 12,
    marginBottom: 16,
    borderWidth: 1,
    borderRadius: 8,
    flexDirection: 'row',
    height: item.probability > 0.7 ? 148 : 76,
    width: Dimensions.get('window').width - 64,        
  },
  mainEntryImage: {
    height: item.probability > 0.7 ? 120 : 48,
    width: item.probability > 0.7 ? 120 : 48,
    borderRadius: 8,
  },
  secondaryEntries: {
  }
});
