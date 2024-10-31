import React, { useState } from 'react';
import { useNavigation } from '@react-navigation/native';
import { ImageBackground, Text, TextInput, TouchableOpacity, View } from "react-native";
import { useFonts, Mulish_800ExtraBold, Mulish_400Regular, Mulish_700Bold } from "@expo-google-fonts/mulish";
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { globalStyles } from '../globalStyles';
import { styles } from "./styles";

export default function Login() {
    const navigation = useNavigation();
    
    const [fontsLoaded] = useFonts({
        Mulish_800ExtraBold,
        Mulish_400Regular,
        Mulish_700Bold
    });

    const [showPassword, setShowPassword] = useState(false);
    const [savePassword, setSavePassword] = useState(false);

    const toggleShowPassword = () => {
        setShowPassword(!showPassword);
    };

    const toggleSavePassword = () => {
        setSavePassword(!savePassword);
    };

    if (!fontsLoaded) {
        return (
            <ImageBackground source={require('../../../assets/background.jpg')} style={globalStyles.background}>
                <View style={styles.container}>
                    <Text style={{color:"#FFFFFF",fontSize:16,}}>Carregando fontes...</Text>
                </View>
            </ImageBackground>
        )
    }

    return (
        <ImageBackground source={require('../../../assets/background.jpg')} style={globalStyles.background}>
            <View style={styles.container}>
                <Text style={[globalStyles.textWhite, globalStyles.textTitle]}>FlowSpace</Text>
                
                <View style={styles.containerLogin}>
                    <View>
                        <Text style={globalStyles.textInputLabel}>Nome de Usuário</Text>
                        <TextInput style={globalStyles.textInput} placeholder="Insira seu nome de usuario" />
                    </View>

                    <View>
                        <Text style={globalStyles.textInputLabel}>Senha</Text>
                        <View style={globalStyles.passwordContainer}>
                            <TextInput
                                secureTextEntry={!showPassword}
                                style={[globalStyles.textInputPassword]}
                                placeholder="Insira sua senha"
                            />
                            <MaterialCommunityIcons
                                name={showPassword ? 'eye-off-outline' : 'eye-outline'}
                                size={24}
                                color="#aaa"
                                onPress={toggleShowPassword}
                                style={globalStyles.icon}
                            />
                        </View>
                    </View>

                    <View style={[globalStyles.textWithIcon]}>
                        <Text>Salvar minha senha</Text>
                        <MaterialCommunityIcons
                            name={savePassword ? 'checkbox-marked-circle-outline' : 'checkbox-blank-circle-outline'}
                            size={24}
                            color="#aaa"
                            onPress={toggleSavePassword}
                            style={[globalStyles.icon]}
                        />
                    </View>

                    <TouchableOpacity style={[globalStyles.defaultButton, globalStyles.buttonGreen]}>
                        <Text style={globalStyles.textWhite}>Entrar</Text>
                    </TouchableOpacity>

                    <TouchableOpacity style={globalStyles.defaultButton} onPress={() => navigation.navigate('Cadastro')}>
                        <Text style={globalStyles.textGreen}>Cadastro</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </ImageBackground>
    );
}