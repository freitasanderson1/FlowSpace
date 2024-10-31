import { StyleSheet } from "react-native";

export const globalStyles = StyleSheet.create({
    background: {
        flex: 1,
        resizeMode: 'cover',
    },
    textInputLabel: {
        color:"#000000",
        fontSize:16,
        fontWeight:"bold",
        paddingBottom: 4,
    },
    textInput:{
        backgroundColor:'#D9D9D9',
        height: 40,
        width: 230,
        borderRadius: 4,
        padding: 12,
        marginBottom: 20,
    },
    passwordInput:{
        backgroundColor:'#D9D9D9',
        borderRadius: 4,
        height: 40,
        width: 230,
    },
    defaultButton:{
        height: 40,
        width: 230,
        alignItems:'center',
        justifyContent: 'center',
        borderRadius: 4,
    },
    buttonGreen:{
        backgroundColor: '#029B75',
    },
    textWhite:{
        color:"#FFFFFF",
        fontSize:16,
        fontFamily: 'Mulish_700Bold',
    },
    textGreen:{
        color:"#029B75",
        fontSize:16,
        fontFamily: 'Mulish_700Bold',
    },
    textTitle:{
        fontSize: 64,
        paddingBottom: 36,
        textShadowColor:'00000025',
        textShadowOffset: {width:0, height:4},
        textShadowRadius: 4,
        fontFamily: 'Mulish_800ExtraBold',
    },
    passwordContainer: {
        flexDirection: 'row',
        alignItems: 'center',
        backgroundColor: '#D9D9D9',
        height: 40,
        width: 230,
        borderRadius: 4,
        paddingHorizontal: 12,
        marginBottom: 20,
    },
    textInputPassword: {
        flex: 1,
    },
    icon: {
        marginLeft: 10,
        color: '#029B75',
    },
    textWithIcon:{
        flexDirection:'row',
        marginBottom:12,
        justifyContent:'center',
        alignItems:'center',
    }
})