import HomePage from "./pages/HomePage.vue";
import LoginPage from "./pages/LoginPage.vue";
import SearchPage from "./pages/SearchPage.vue";
import ProfilePage from "./pages/ProfilePage.vue";
import ProfileEdittingPage from "./pages/ProfileEdittingPage.vue";
import { getToken } from "./apis/auth";

import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: "/",
        name: "home",
        component: HomePage,
    },
    {
        path: "/search_result",
        name: "search_result",
        component: SearchPage,
    },
    {
        path: "/profile",
        name: "profile",
        component: ProfilePage,
    },
    {
        path: "/profile/edit",
        name: "profile_edit",
        component: ProfileEdittingPage,
    },
    {
        path: "/login",
        name: "login",
        component: LoginPage,
    },
];

const router = createRouter({
    routes: routes,
    history: createWebHistory(),
});

/* 路由守卫 */
router.beforeEach((to) => {
    /* 如果访问的不是 login 并且没有 token，则要求登录 */
    if (to.name !== "login" && !getToken()) {
        return { name: "login" };
    }
    /* 如果访问的是 login 并且有 token，则跳转到 home */
    if (to.name == "login" && getToken()) {
        return { name: "home" };
    }
});

export { router };