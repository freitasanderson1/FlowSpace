import React, { useState } from 'react';
import { ImageBackground, Text, TextInput, TouchableOpacity, View } from "react-native";
import { useNavigation } from '@react-navigation/native'; // Importação do hook de navegação
import { styles } from "./styles";
import { useFonts, Mulish_800ExtraBold, Mulish_400Regular, Mulish_700Bold } from "@expo-google-fonts/mulish";
import { MaterialCommunityIcons } from '@expo/vector-icons';

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
        return <Text>Carregando fontes...</Text>;
    }

    return (
        <ImageBackground source={require('../../../assets/background.jpg')} style={styles.background}>
            <View style={styles.container}>
                <Text style={[styles.textWhite, styles.textTitle]}>FlowSpace</Text>
                
                <View style={styles.containerLogin}>
                    <View>
                        <Text style={styles.textInputLabel}>Nome</Text>
                        <TextInput style={styles.textInput} placeholder="Insira seu nome" />
                    </View>

                    <View>
                        <Text style={styles.textInputLabel}>Email</Text>
                        <TextInput style={styles.textInput} placeholder="Insira seu email" keyboardType='email'/>
                    </View>

                    <View>
                        <Text style={styles.textInputLabel}>Senha</Text>
                        <View style={styles.passwordContainer}>
                            <TextInput
                                secureTextEntry={!showPassword}
                                style={[styles.textInputPassword]}
                                placeholder="Insira sua senha"
                            />
                            <MaterialCommunityIcons
                                name={showPassword ? 'eye-off-outline' : 'eye-outline'}
                                size={24}
                                color="#aaa"
                                onPress={toggleShowPassword}
                                style={styles.icon}
                            />
                        </View>
                    </View>

                    <TouchableOpacity style={[styles.defaultButton, styles.buttonGreen]}>
                        <Text style={styles.textWhite}>Cadastrar-se</Text>
                    </TouchableOpacity>

                    <TouchableOpacity style={styles.defaultButton} onPress={() => navigation.navigate('Login')}>
                        <Text style={styles.textGreen}>Já tem cadastro? Faça Login</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </ImageBackground>
    );
}