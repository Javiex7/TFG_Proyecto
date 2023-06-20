import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";

import BootstrapVue from "bootstrap-vue-3";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-icons/font/bootstrap-icons.css";

import "./assets/main.css";

const app = createApp(App).use(store).use(router, axios).use(BootstrapVue);

app.config.globalProperties.$userProfile = null;
app.mount("#app");
