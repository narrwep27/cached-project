import Client from "./api";

export const Register = async (userInfo) => {
    const res = await Client.post(`register`, userInfo);
    return res.data;
};

export const Login = async (userInfo) => {
    const res = await Client.post('login', userInfo);
    return res.data;
};

export const LoadUser = async (userId) => {
    const res = await Client.get(`user/read/${userId}`)
    return res.data;
};