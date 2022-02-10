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

export const LoadUser = async (uesrId) => {
    try {
        const res = await Client.get(`user/read/${userId}`)
        return res.data;
    } catch (error) {
        throw error;
    }
};