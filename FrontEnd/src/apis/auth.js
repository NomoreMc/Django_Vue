/* 获取 local storage 中的 jwt token */
export function getJWTToken() {
    return localStorage.getItem('jwtToken');
}

/* 将获取到的 jwt token 放入 local storage 中 */
export function setJWTToken(jwt) {
    localStorage.setItem('jwtToken', jwt);
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
export async function register(email, username, password) {
    const result = await request("/api/auth/local/register", {
        method: "POST",
        auth: false,
        body: {
            email,
            username,
            password,
            name: username,
        },
    });
    setJWTToken(result.jwt);
    saveUser(result.user);
    return result.user;
}