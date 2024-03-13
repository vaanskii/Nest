import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore({
    id: 'user',

    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            email: null,
            username: null,
            mobile_number: null,
            access: null,
            refresh: null,
            profile_picture: null
        }
    }),

    actions: {
        initStore() {
            if (localStorage.getItem('user.access')) {
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.id = localStorage.getItem('user.id')
                this.user.username = localStorage.getItem('user.username')
                this.user.email = localStorage.getItem('user.email')
                this.user.mobile_number = localStorage.getItem('user.mobile_number')
                this.user.profile_picture = localStorage.getItem('user.profile_picture')
                this.user.isAuthenticated = true

                this.refreshToken()
            }
        },

        setToken(data) {
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)
        },

        removeToken() {
            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = null
            this.user.username = null
            this.user.mobile_number = null
            this.user.email = null
            this.user.profile_picture = null

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.username', '')
            localStorage.setItem('user.mobile_number', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.profile_picture', '')
        },

        setUserInfo(user) {
            this.user.id = user.id
            this.user.username = user.username
            this.user.email = user.email
            this.user.mobile_number = user.mobile_number
            this.user.profile_picture = user.profile_picture

            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.username', this.user.username)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.mobile_number', this.user.mobile_number)
            localStorage.setItem('user.profile_picture', this.user.profile_picture)
        },

        refreshToken() {
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    this.user.access = response.data.access

                    localStorage.setItem('user.access', response.data.access)

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    console.log(error)
                    this.removeToken()
                })
        },
    }
})