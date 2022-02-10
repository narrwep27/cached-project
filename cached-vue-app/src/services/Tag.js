import Client from "./api";

export const CreateTag = async (newTag) => {
    try {
        const res = await Client.post(`tag/create`, newTag);
        return res.data;
    } catch (error) {
        throw error;
    }
};

export const EditTag = async (tagId, editedTag) => {
    try {
        const res = await Client.put(`tag/${tagId}`, editedTag);
        return res.data;
    } catch (error) {
        throw error;
    }
};

export const DeleteTag = async (tagId) => {
    try {
        const res = await Client.delete(`tag/${tagId}`);
        return res.data;
    } catch (error) {
        throw error;
    }
}