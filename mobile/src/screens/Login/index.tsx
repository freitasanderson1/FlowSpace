import React, { useState } from 'react';
import { useNavigation } from '@react-navigation/native';
import { ImageBackground, Text, TextInput, TouchableOpacity, View } from "react-native";
import { useFonts, Mulish_800ExtraBold, Mulish_400Regular, Mulish_700Bold } from "@expo-google-fonts/mulish";
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { styles } from "./styles";

export default function Login() {
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
                        <Text style={styles.textInputLabel}>Nome de Usuário</Text>
                        <TextInput style={styles.textInput} placeholder="Insira seu nome de usuario" />
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
                        <Text style={styles.textWhite}>Entrar</Text>
                    </TouchableOpacity>

                    <TouchableOpacity style={styles.defaultButton} onPress={() => navigation.navigate('Cadastro')}>
                        <Text style={styles.textGreen}>Cadastro</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </ImageBackground>
    );
}