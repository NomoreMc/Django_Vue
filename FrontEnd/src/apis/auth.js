import { request } from "../utils/request";

/* 获取 local storage 中的 jwt */
export function getJWTToken() {
    return localStorage.getItem('jwtToken');
}

/* 将获取到的 jwt 放入 local storage 中 */
export function setJWTToken(jwt) {
    localStorage.setItem('jwtToken', jwt);
}

/* 将获取到的 token 放入 local storage 中 */
export function setToken(token) {
    localStorage.setItem('token', token);
}

/* 获取 local storage 中的 token */
export function getToken() {
    return localStorage.getItem('token');
}

/* 保存 user 到 local storage 中 */
export function saveUser(user) {
    localStorage.setItem('user', JSON.stringify(user));
}

/* 从 local storage 中获取 user */
export function getUser() {
    return JSON.parse(localStorage.getItem('user'));
}

/* 向后端发送注册请求 */
export async function register(username, password, email) {
    const result = await request("/Account/api/user/register/", {
        method: "POST",
        auth: false,
        body: {
            email,
            username,
            password,
            // name: username,
        },
    });
    // setJWTToken(result.jwt);
    // setToken(result.token);
    // saveUser(result.user);
    // return result.user;

    return result.user.username;
}

export async function login(username, password) {
    const result = await request("/api/auth/login/", {
        method: "POST",
        auth: false,
        body: {
            username,
            password,
        },
    });
    setToken(result.token);
    saveUser(result.user);
    return result.user.username;
}