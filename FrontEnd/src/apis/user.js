import { request } from '../utils/request'
import { saveUser } from './auth';

// 暂未使用
export async function changeUser(user) {
    return null;
    const response = await request(`/api/users/${getUser().id}`, {
        method: "PUT",
        body: user,
    });

    saveUser(response);
    return response;
}