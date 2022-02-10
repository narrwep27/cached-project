import Client from "./api";

export const Register = async (userInfo) => {
    try {
        const res = await Client.post(`register`, userInfo);
        return res.data;
    } catch (error) {
        throw error;
    }
};

export const Login = async (userInfo) => {
    try {
        const res = await Client.post('login', userInfo);
        return res.data;
    } catch (error) {
        throw error;
    }
};