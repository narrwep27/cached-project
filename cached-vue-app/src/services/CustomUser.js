import Client from "./api";

export const Register = async (userInfo) => {
    try {
        const res = await Client.post(`register`, userInfo);
        return res.data;
    } catch (error) {
        return {
            status: error.response.status,
            statusText: error.response.statusText,
            detail: error.response.data.email[0]}
    }
};

export const Login = async (userInfo) => {
    try {
        const res = await Client.post('login', userInfo);
        localStorage.setItem('accessToken', res.data.access);
        localStorage.setItem('refreshToken', res.data.refresh);
        localStorage.setItem('user_id', res.data.user_id);
        Client.interceptors.request.use((config) => {
            const token = localStorage.getItem('accessToken')
            if (token) {
                config.headers['Authorization'] = `JWT ${token}`
            }
            return config
        })
        return res.data;
    } catch (error) {
        return { 
            status: error.response.status,
            statusText: error.response.statusText,
            detail: error.response.data.detail
        }
    }
};

export const LoadUser = async (userId) => {
    const res = await Client.get(`user/read/${userId}`)
    return res.data;
};