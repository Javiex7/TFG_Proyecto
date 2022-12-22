import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import BootstrapVue from "bootstrap-vue-3";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-icons/font/bootstrap-icons.css";

createApp(App).use(router).use(BootstrapVue).mount("#app");
