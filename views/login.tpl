% rebase("layout.tpl", title="Login")

<div class="container">
  <div class="row">
    <div class="twelve columns" style="margin-top: 10%">
      <h4 style="text-align: center">Login</h4>
    </div>
  </div>
  <form action="/login" method="POST" style="margin-left: 35%">
    <fieldset>
      <div class="row", style="margin-top: 5%">
        <div class="six columns">
          <label for="username">Username</label>
          <input class="u-full-width" id="username" type="text" placeholder="johnappleseed" name="username">
        </div>
      </div>
      <div class="row">
        <div class="six columns">
          <label for="password">Password</label>
          <input class="u-full-width" id="password" type="password"  name="password">
        </div>
      </div>
      <input class="button-primary" style="margin: 3%; margin-left: 0%" type="submit" value="Submit">

    </fieldset>
  </form>
  <div class="row" style="margin-left: 35%">
    <!-- <a href="https://www.google.com">Don't have an account? Register Here</a> -->
  </div>
</div>
