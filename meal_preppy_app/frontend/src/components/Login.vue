<template>
  <div class="container">
    <div class="columns is-centered">
      <form class="card column is-10-mobile is-4 py-6">
        <h1 class="pb-6 is-size-4 has-text-weight-bold">Login</h1>
        <FormField
          class="column is-10"
          label="username"
          labelText="Username"
          inputType="text"
          required="required"
          v-model="username"
        />
        <FormField
          class="column is-10"
          label="password"
          labelText="Password"
          inputType="password"
          required="required"
          v-model="password"
        />
        <Button @click="authenticate" buttonTxt="Login" />
      </form>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import FormField from './form_components/FormField.vue';
import Button from './form_components/Button.vue';

// TODO! Fix form offset to left in mobile view

export default {
  name: 'Login',
  components: {
    FormField,
    Button,
  },
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    authenticate(e) {
      const path = 'http://localhost:5000/users/login';

      e.preventDefault();

      axios
        .post(
          path,
          {
            username: this.username,
            password: this.password,
          },
          // This is added for CORS
          {
            withCredentials: true,
          },
        )
        .then((res) => {
          localStorage.setItem('token', res.data.token);
          if (res.data.token) {
            this.$store.commit('setAuthentication', true);
            this.$router.push({ name: 'Home' });
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
