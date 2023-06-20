import { createRouter, createWebHistory } from "vue-router";

// Views
import HomeView from "../views/HomeView.vue";
import RegisterView from "../views/RegisterView.vue";
import LoginView from "../views/LoginView.vue";
import UserProfileView from "../views/UserProfileView.vue";
import CategoryDetailView from "../views/CategoryDetailView.vue";
import MakeTestView from "../views/MakeTestView.vue";
import PackView from "../views/PackView.vue";
import PageNotFoundView from "../views/PageNotFoundView.vue";
import GeneralPracticeView from "../views/GeneralPracticeView.vue";
import GroupRankingView from "../views/GroupRankingView.vue";

// Components
import ListCategories from "../components/categories/ListCategories";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
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
    path: "/packs/:packId",
    component: PackView,
  },
  {
    path: "/general-practice",
    component: GeneralPracticeView,
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
    path: "/ranking",
    name: "ranking",
    component: GroupRankingView,
  },
  {
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
