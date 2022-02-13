import Client from "./api";

export const CreateExpense = async (newExp) => {
    try {
        const res = await Client.post(`expense/create`, newExp);
        return res.data;
    } catch (error) {
        return error.response;
    }
};

export const EditExpense = async (expId, expEdit) => {
    try {
        const res = await Client.patch(`expense/update/${expId}`, expEdit);
        return res.data;
    } catch (error) {
        return error.response;
    }
};

export const DeleteExpense = async (expId) => {
    try {
        const res = await Client.delete(`expense/update/${expId}`);
        return res.data;
    } catch (error) {
        return error.response;
    }
};