import Client from "./api";

export const CreateGoal = async (newGoal) => {
    try {
        const res = await Client.post(`goal/create`, newGoal);
        return res.data;
    } catch (error) {
        throw error;
    };
};

export const EditGoal = async (goalId, goalEdit) => {
    try {
        const res = await Client.put(`goal/update/${goalId}`, goalEdit);
        return res.data;
    } catch (error) {
        throw error;
    };
};

export const DeleteGoal = async (goalId) => {
    try {
        const res = await Client.delete(`goal/update/${goalId}`);
        return res.data;
    } catch (error) {
        throw error;
    };
};