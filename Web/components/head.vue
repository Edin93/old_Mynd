<template>
  <div>
    <sui-menu fixed>
      <sui-container>
        <a is="sui-menu-item" href="/" class="header">
          <img src="../assets/images/logo.png" class="logo" />
          Mynd
        </a>
      </sui-container>
      <sui-menu-menu position="right">
        <a @click.native="toggleJoin" is="sui-menu-item" class="header">
          Join
        </a>
        <a @click.native="toggleLogin" is="sui-menu-item" class="header">
          Login
        </a>
        <sui-menu-item>
          <sui-input transparent icon="search" placeholder="Search..." />
        </sui-menu-item>
      </sui-menu-menu>
    </sui-menu>

    <sui-modal size="mini" v-model="login">
      <sui-modal-header>Login</sui-modal-header>

      <sui-form>
        <sui-segment>
          <sui-form-field>
            <sui-input
              type="email"
              placeholder="E-mail address"
              icon="user"
              icon-position="left"
            />
          </sui-form-field>
          <sui-form-field>
            <sui-input
              type="password"
              placeholder="Password"
              icon="lock"
              icon-position="left"
            />
          </sui-form-field>
          <sui-button size="large" fluid>Login</sui-button>
        </sui-segment>
      </sui-form>

      <sui-message>New to Mynd? <a @click="toggle">Sign Up</a> </sui-message>
    </sui-modal>
    <sui-modal size="mini" v-model="join">
      <sui-modal-header>Join Mynd</sui-modal-header>

      <sui-form>
        <sui-segment>
          <sui-form-field>
            <sui-input type="email" placeholder="E-mail address" />
          </sui-form-field>
          <sui-form-field>
            <sui-input type="username" placeholder="Username" />
          </sui-form-field>
          <sui-form-field>
            <sui-input type="password" placeholder="Password" />
          </sui-form-field>
          <sui-form-field>
            <sui-dropdown
              placeholder="Gender"
              selection
              :options="options"
              v-model="current"
            />
          </sui-form-field>

          <sui-button size="large" fluid>Join</sui-button>
        </sui-segment>
      </sui-form>
      <sui-message>Already on Mynd? <a @click="toggle">Login</a></sui-message>
    </sui-modal>
  </div>
</template>

<script>
export default {
  name: "Head",
  data() {
    return {
      join: false,
      login: false,
      current: null,
      options: [
        {
          text: "Male",
          value: 1
        },
        {
          text: "Female",
          value: 2
        }
      ]
    };
  },
  methods: {
    toggleJoin() {
      this.join = !this.join;
    },
    toggleLogin() {
      this.login = !this.login;
    },
    toggle() {
      this.join = !this.join;
      this.login = !this.login;
    }
  }
};
</script>

<style scoped>
.message {
  margin-top: 0;
}
.button {
  color: aliceblue;
  background: #5a4fdc;
}
.button:hover {
  color: antiquewhite;
  background: #6e64d8;
}
a {
  color: #5a4fdc;
}
</style>
