import { getJWTToken } from '../apis/auth';

export async function request(url, { method = 'GET', body, headers, auth = true } = {}) {
    const resp = await fetch(url, {
        method,
        headers: {
            'Content-Type': 'application/json',
            ...(auth && { Authorization: `Bearer ${getJWTToken()}` }),
            ...headers,
        },
        ...(body && { body: JSON.stringify(body) }),
    });

    const result = await resp.json();
    return result;
};