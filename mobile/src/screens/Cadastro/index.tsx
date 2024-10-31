import React, { useState } from 'react';
import { ImageBackground, Text, TextInput, TouchableOpacity, View } from "react-native";
import { useNavigation } from '@react-navigation/native'; // Importação do hook de navegação
import { useFonts, Mulish_800ExtraBold, Mulish_400Regular, Mulish_700Bold } from "@expo-google-fonts/mulish";
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { globalStyles } from '../globalStyles';
import { styles } from "./styles";

export default function Cadastro() {
    const navigation = useNavigation();

    const [fontsLoaded] = useFonts({
        Mulish_800ExtraBold,
        Mulish_400Regular,
        Mulish_700Bold
    });

    const [showPassword, setShowPassword] = useState(false);

    const toggleShowPassword = () => {
        setShowPassword(!showPassword);
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
                
                <View style={styles.containerCadastro}>
                    <View>
                        <Text style={globalStyles.textInputLabel}>Nome</Text>
                        <TextInput style={globalStyles.textInput} placeholder="Insira seu nome" />
                    </View>

                    <View>
                        <Text style={globalStyles.textInputLabel}>Email</Text>
                        <TextInput style={globalStyles.textInput} placeholder="Insira seu email" keyboardType='email'/>
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

                    <TouchableOpacity style={[globalStyles.defaultButton, globalStyles.buttonGreen]}>
                        <Text style={globalStyles.textWhite}>Cadastrar-se</Text>
                    </TouchableOpacity>

                    <TouchableOpacity style={globalStyles.defaultButton} onPress={() => navigation.navigate('Login')}>
                        <Text style={globalStyles.textGreen}>Já tem cadastro? Faça Login</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </ImageBackground>
    );
}