import Axios from 'axios';

const Client = Axios.create({
    baseURL: 'http://localhost:8000/api/cached/',
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