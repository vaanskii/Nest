<template>
    <div class="flex justify-center">
    <div class="main-right ">
        <div class="mt-12">
            <form class="space-y-6" v-on:submit.prevent="submitForm">
                <div class="p-4 flex justify-center">
                    <div class="relative w-[280px] md:w-[450px] min-w-[200px]">
                        <input
                            type="password"
                            v-model="form.old_password"
                            class="peer h-14 w-[280px] md:w-[450px] mr-16 overflow-hidden resize-none border-b border-gray-400 bg-transparent pb-1.5 pt-3 pl-4 font-sans text-sm font-normal text-gray-900 outline outline-0 transition-all focus:border-gray-900 focus:outline-0"
                            placeholder=" "
                            id="username"
                        ></input>
                        <label
                            for="username"
                            class="after:content[' '] uppercase after:border-t-[1px] text-black pointer-events-none absolute left-0 -top-[5.5px] flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-500 transition-all after:absolute after:-bottom-1.5 after:left-0 after:w-full after:scale-x-0 after:border-b-[1.5px] after:border-gray-900 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] peer-placeholder-shown:text-blue-gray-500 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-gray-900 peer-focus:after:scale-x-100 peer-focus:after:border-gray-900 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500"
                        >
                            old password
                        </label>
                    </div>
                </div>

                <div class="p-4 flex justify-center">
                    <div class="relative w-[280px] md:w-[450px] min-w-[200px]">
                        <input
                            type="password"
                            v-model="form.new_password1"
                            class="peer h-14 w-[280px] md:w-[450px] mr-16 overflow-hidden resize-none border-b border-gray-400 bg-transparent pb-1.5 pt-3 pl-4 font-sans text-sm font-normal text-gray-900 outline outline-0 transition-all focus:border-gray-900 focus:outline-0"
                            placeholder=" "
                            id="username"
                        ></input>
                        <label
                            for="username"
                            class="after:content[' '] uppercase after:border-t-[1px] text-black pointer-events-none absolute left-0 -top-[5.5px] flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-500 transition-all after:absolute after:-bottom-1.5 after:left-0 after:w-full after:scale-x-0 after:border-b-[1.5px] after:border-gray-900 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] peer-placeholder-shown:text-blue-gray-500 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-gray-900 peer-focus:after:scale-x-100 peer-focus:after:border-gray-900 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500"
                        >
                            new password
                        </label>
                    </div>
                </div>

                <div class="p-4 flex justify-center">
                    <div class="relative w-[280px] md:w-[450px] min-w-[200px]">
                        <input
                            type="password"
                            v-model="form.new_password2"
                            class="peer h-14 w-[280px] md:w-[450px] mr-16 overflow-hidden resize-none border-b border-gray-400 bg-transparent pb-1.5 pt-3 pl-4 font-sans text-sm font-normal text-gray-900 outline outline-0 transition-all focus:border-gray-900 focus:outline-0"
                            placeholder=" "
                            id="username"
                        ></input>
                        <label
                            for="username"
                            class="after:content[' '] uppercase after:border-t-[1px] text-black pointer-events-none absolute left-0 -top-[5.5px] flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-500 transition-all after:absolute after:-bottom-1.5 after:left-0 after:w-full after:scale-x-0 after:border-b-[1.5px] after:border-gray-900 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] peer-placeholder-shown:text-blue-gray-500 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-gray-900 peer-focus:after:scale-x-100 peer-focus:after:border-gray-900 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500"
                        >
                            confirm password
                        </label>
                    </div>
                </div>

                <template v-if="errors.length > 0">
                    <div class="bg-red-300 text-white rounded-lg p-6">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                </template>

                <div>
                    <button type="submit" class="relative h-[50px] w-72 overflow-hidden border border-black bg-white px-3 text-black shadow-2xl transition-all before:absolute before:bottom-0 before:left-0 before:top-0 before:z-0 before:h-full before:w-0 before:bg-black before:transition-all before:duration-500 hover:text-white hover:shadow-black rounded-md hover:before:left-0 hover:before:w-full"><span class="relative z-10">Change password</span></button>
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
                old_password: '',
                new_password1: '',
                new_password2: '',
            },
            errors: [],
        };
    },
    methods: {
        submitForm() {
            this.errors = [];
            
            if (this.form.new_password1 !== this.form.new_password2) {
                this.errors.push('The passwords do not match');
            }

            if (this.errors.length === 0) {
                let formData = new FormData();
                formData.append('old_password', this.form.old_password);
                formData.append('new_password1', this.form.new_password1);
                formData.append('new_password2', this.form.new_password2);

                axios
                    .post('/api/editpassword/', formData, {
                        headers: {
                            "Content-Type": "multipart/form-data"
                        }
                    })
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'The password is changed', 'bg-emerald-500');

                            this.$router.push(`/profile/${this.userStore.user.id}`);
                            this.$router.back()
                        }
                        else {
                            const data = JSON.parse(response.data.message);
                            for (const key in data) {
                                this.errors.push(data[key][0].message);
                            }
                        }
                    })
                    .catch(error => {
                        console.log('error', error);
                    });
            }
        }

    },
    components: { RouterLink }
}

</script>