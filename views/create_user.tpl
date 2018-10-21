% rebase("layout.tpl", title="Store App - New User")
% if "permissions" in sess and sess["permissions"] == "MANAGER":
<div class="container">
  <div class="row">
    <div class="twelve column" style="margin-top: 10%">
      <h4 style="text-align: center">Create A New User</h4>
    </div>
  </div>
  <form action="/create_user" method="POST">
    <fieldset>
      <div class="row", style="margin-top: 5%;">
        <div class="six columns" style="margin-left: 25%; text-align: center;">
          <label for="username">Username</label>
          <input class="u-full-width" id="username" type="text" name="username">
        </div>

        <div class="row", style="margin-top: 5%; text-align: center;">
          <div class="six columns" style="margin-left: 25%">
            <label for="role">Role</label>
            <select class="u-full-width" id="role" name="role">
              <option value="CASHIER">Cashier</option>
              <option value="MANAGER">Manager</option>
            </select>
          </div>

        </div>
        <a class="button" href="/", style="margin: 3%; margin-left: 25%">Cancel</a>
        <input class="button-primary" type="submit" value="Create">

      </fieldset>
    </form>
  </div>
  % else:
  % include('denied.tpl')