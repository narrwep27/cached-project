import Client from "./api";

export const CreateTag = async (newTag) => {
    try {
        const res = await Client.post(`tag/create`, newTag);
        return res.data;
    } catch (error) {
        return error.response;
    }
};

export const EditTag = async (tagId, tagEdit) => {
    try {
        const res = await Client.patch(`tag/update/${tagId}`, tagEdit);
        return res.data;
    } catch (error) {
        return error.response;
    }
};

export const DeleteTag = async (tagId) => {
    try {
        const res = await Client.delete(`tag/update/${tagId}`);
        return res.data;
    } catch (error) {
        return error.response;
    }
}