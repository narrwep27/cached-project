import Axios from 'axios';

const baseURL = 'http://localhost:8000/api/cached/'

const Client = Axios.create({
    baseURL: baseURL,
    timeout: 5000,
    headers: {
        Authorization: localStorage.getItem('access_token')
            ? 'JWT ' + localStorage.getItem('access_token')
            : null,
        'Content-Type': 'application/json',
        accept: 'application/json'
    }
});

export default Client;