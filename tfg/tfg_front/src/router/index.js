import { createRouter, createWebHistory } from "vue-router";

// Views
import HomeView from "../views/HomeView.vue";
import RegisterView from "../views/RegisterView.vue";
import LoginView from "../views/LoginView.vue";
import UserProfileView from "../views/UserProfileView.vue";
import CategoryDetailView from "../views/CategoryDetailView.vue";
import MakeTestView from "../views/MakeTestView.vue";
import PageNotFoundView from "../views/PageNotFoundView.vue";

// Components
import ListCategories from "../components/categories/ListCategories";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    // Try to use the ListCategories component through the HomeView instead
    path: "/categories",
    name: "categories",
    component: ListCategories,
  },
  {
    path: "/categories/:categoryId",
    component: CategoryDetailView,
  },
  {
    path: "/quizzes/:quizId",
    component: MakeTestView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/register",
    name: "register",
    component: RegisterView,
  },
  {
    path: "/profile",
    name: "profile",
    component: UserProfileView,
  },
  {
    // path: "*",
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: PageNotFoundView,
    meta: {
      requiresAuth: false,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
