<template>
    <form class="space-y-4 md:space-y-6 bg-gray-600" v-on:submit.prevent="submitForm">
        <div>
            <input type="email" v-model="form.email" placeholder="Enter email">
        </div>
        <div>
            <input type="text" v-model="form.username" placeholder="Enter username">
        </div>
        <div>
            <input type="tel" v-model="form.mobile_number" placeholder="Enter mobile number">
        </div>
        <div>
            <input type="password" v-model="form.password1" placeholder="Enter password">
        </div>
        <div>
            <input type="password" v-model="form.password2" placeholder="Confirm password">
        </div>
        <button type="submit" class="p-4 bg-gray-900 rounded-lg">Create account</button>
        
        <template v-if="errors.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-6">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
        </template>
    </form>
</template>

<script>
import axios from 'axios'
export default{
    data() {
        return {
            form: {
                email: '',
                username: '',
                password1: '',
                password2: '',
                mobile_number: ''
            },
            errors : []
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('your email is missing')
            }

            if (this.form.username === '') {
                this.errors.push('your username is missing')
            }

            if (this.form.password1 === '') {
                this.errors.push('your password is missing')
            }
            if (this.form.mobile_number === '') {
                this.errors.push('your mobile number is missing')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The password does not match')
            }
            if (this.errors.length === 0) {
               axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {

                            this.form.email = ''
                            this.form.username = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                            this.form.mobile_number = ''
                        } else{
                            const data = JSON.parse(response.data.message)
                            for (const key in data) {
                                this.errors.push(data[key][0].message)
                            }
                        }
                        console.log(response.data)

                    })
                    .catch(error => {
                        console.log('error',error)
                    })
            }
        }
    }
}
</script>