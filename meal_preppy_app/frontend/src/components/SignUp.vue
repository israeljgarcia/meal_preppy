<template>
  <div class="container mt-6">
    <div class="columns is-centered">
      <div
        class="card pt-6 pb-6 column is-4 is-10-mobile my-0 mx-auto"
      >
        <h1 class="pb-6 is-size-4 has-text-weight-bold">Sign Up</h1>
        <div class="columns has-text-left is-centered">
          <form
            class="column is-10 is-12-mobile"
            method="POST"
            action="http://localhost:5000/users/signup"
          >
            <div class="field">
              <label class="label" for="firstName">First Name</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  name="firstName"
                  id="firstName"
                  required
                />
              </div>
            </div>

            <div class="field">
              <label class="label" for="lastName">Last Name</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  name="lastName"
                  id="lastName"
                  required
                />
              </div>
            </div>

            <div class="field">
              <label class="label" for="username">Username</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  name="username"
                  id="username"
                  required
                />
              </div>
            </div>

            <div class="field">
              <label for="email" class="label">Email</label>
              <div class="control">
                <input
                  class="input"
                  type="email"
                  name="email"
                  id="email"
                  required
                />
              </div>
            </div>

            <div class="field">
              <label for="password" class="label">Password</label>
              <div class="control">
                <input
                  class="input"
                  type="password"
                  name="password"
                  id="password"
                />
              </div>
            </div>

            <p class="has-text-centered">Already have an accout? <a href="/login">Log in</a>.</p>

            <div class="columns is-centered mt-4">
              <button
                class="button has-text-centered is-dark mt-2"
                type="submit"
              >
                Add Ingredient
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
