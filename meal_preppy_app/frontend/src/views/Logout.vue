<template>
  <div></div>
</template>
<script>
export default {
  name: 'Logout',
  methods: {
    logout() {
      localStorage.removeItem('token');
      this.$store.commit('setAuthentication', false);
      this.$router.push('LoginForm');
    },
  },
  created() {
    this.logout();
  },
};
</script>
