<template>
    <div class="flex justify-center">
        <div class="main-right ">
            <div class="mt-12">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div class="p-4 flex justify-center">
                        <div class="relative w-[450px] min-w-[200px]">
                            <input
                                type="text"
                                v-model="form.username"
                                class="peer h-14 w-[450px] mr-16 overflow-hidden resize-none border-b border-gray-400 bg-transparent pb-1.5 pt-3 pl-4 font-sans text-sm font-normal text-gray-900 outline outline-0 transition-all focus:border-gray-900 focus:outline-0"
                                placeholder=" "
                                id="username"
                            ></input>
                            <label
                                for="username"
                                class="after:content[' '] after:border-t-[1px] text-black pointer-events-none absolute left-0 -top-[5.5px] flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-500 transition-all after:absolute after:-bottom-1.5 after:left-0 after:w-full after:scale-x-0 after:border-b-[1.5px] after:border-gray-900 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] peer-placeholder-shown:text-blue-gray-500 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-gray-900 peer-focus:after:scale-x-100 peer-focus:after:border-gray-900 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500"
                            >
                                Username
                            </label>
                        </div>
                    </div>

                    <div class="p-4 flex justify-center mb-12">
                        <div class="relative w-[450px] min-w-[200px]">
                            <input
                                type="email"
                                v-model="form.email"
                                class="peer h-14 w-[450px] mr-16 overflow-hidden resize-none border-b border-gray-400 bg-transparent pb-1.5 pt-3 pl-4 font-sans text-sm font-normal text-gray-900 outline outline-0 transition-all focus:border-gray-900 focus:outline-0"
                                placeholder=" "
                                id="email"
                            ></input>
                            <label
                                for="email"
                                class="after:content[' '] text-black pointer-events-none absolute left-0 -top-[5.5px] flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-500 transition-all after:absolute after:-bottom-1.5 after:left-0 after:w-full after:scale-x-0 after:border-b-[1.5px] after:border-t-[1px] after:border-gray-900 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] peer-placeholder-shown:text-blue-gray-500 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-gray-900 peer-focus:after:scale-x-100 peer-focus:after:border-gray-900 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500"
                            >
                                Email
                            </label>
                        </div>
                    </div>

                    <div class="p-4 flex justify-center mb-12">
                        <div class="relative w-[450px] min-w-[200px]">
                            <input
                                type="tel"
                                v-model="form.mobile_number"
                                class="peer h-14 w-[450px] mr-16 overflow-hidden resize-none border-b border-gray-400 bg-transparent pb-1.5 pt-3 pl-4 font-sans text-sm font-normal text-gray-900 outline outline-0 transition-all focus:border-gray-900 focus:outline-0"
                                placeholder=" "
                                id="mobile-number"
                            ></input>
                            <label
                                for="mobile-number"
                                class="after:content[' '] after:border-t-[1px] text-black pointer-events-none absolute left-0 -top-[5.5px] flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-500 transition-all after:absolute after:-bottom-1.5 after:left-0 after:w-full after:scale-x-0 after:border-b-[1.5px] after:border-gray-900 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] peer-placeholder-shown:text-blue-gray-500 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-gray-900 peer-focus:after:scale-x-100 peer-focus:after:border-gray-900 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500"
                            >
                                Mobile number
                            </label>
                        </div>
                    </div>
                    <div>
                        <label for="">Upload image</label>
                        <input type="file" ref="file">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button type="submit" class="relative h-[50px] w-72 overflow-hidden border border-black bg-white px-3 text-black shadow-2xl transition-all before:absolute before:bottom-0 before:left-0 before:top-0 before:z-0 before:h-full before:w-0 before:bg-black before:transition-all before:duration-500 hover:text-white hover:shadow-black rounded-md hover:before:left-0 hover:before:w-full"><span class="relative z-10">Save changes</span></button>
                    </div>
                </form>

            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import { useToastStore } from '@/store/toast';
import { useUserStore } from '@/store/user';
import { RouterLink } from 'vue-router';

export default{
    setup() {
        const toastStore = useToastStore();
        const userStore = useUserStore();
        return {
            toastStore,
            userStore
        };
    },
    data() {
        return {
            form: {
                email: this.userStore.user.email,
                username: this.userStore.user.username,
                mobile_number: this.userStore.user.mobile_number,
            },
            errors: [],
        };
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.username === '') {
                this.errors.push('Your username is missing')
            }
            if (this.form.mobile_number === '') {
                this.errors.push('Your mobile number is missing')
            }

            if (this.errors.length === 0) {
                let formData = new FormData()
                formData.append('profile_picture', this.$refs.file.files[0])
                formData.append('username', this.form.username)
                formData.append('email', this.form.email)
                formData.append('mobile_number', this.form.mobile_number)

                axios
                    .post('/api/editprofile/', formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        }
                    })
                    .then(response => {
                        if (response.data.message === 'Information updated') {
                            this.toastStore.showToast(5000, 'The information was saved', 'bg-emerald-500')

                            this.userStore.setUserInfo({
                                id: this.userStore.user.id,
                                username: this.form.username,
                                email: this.form.email,
                                mobile_number: this.form.mobile_number,
                                profile_picture: response.data.get_profile_picture
                            })
                            this.$router.back()
                        } else {
                            this.toastStore.showToast(5000, `${response.data.message}. Please try again`, 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    },
    components: { RouterLink }
}

</script>