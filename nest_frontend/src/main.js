import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

axios.defaults.baseURL = "https://vaanskii.pythonanywhere.com"
const app = createApp(App)

app.use(createPinia())
app.use(router, axios)

app.mount('#app')