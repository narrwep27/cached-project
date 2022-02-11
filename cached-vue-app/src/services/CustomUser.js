import Client from "./api";

export const Register = async (userInfo) => {
    try {
        const res = await Client.post(`register`, userInfo);
        return res.data;
    } catch (error) {
        return error.response.data.email[0]
    }
};

export const Login = async (userInfo) => {
    const res = await Client.post('login', userInfo);
    return res.data;
};

export const LoadUser = async (userId) => {
    const res = await Client.get(`user/read/${userId}`)
    return res.data;
};