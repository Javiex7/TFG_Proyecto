import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";

import BootstrapVue from "bootstrap-vue-3";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-icons/font/bootstrap-icons.css";

import "./assets/main.css";

createApp(App).use(store).use(router, axios).use(BootstrapVue).mount("#app");
