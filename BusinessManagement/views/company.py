import pycountry
from flask import Blueprint, render_template, request, flash, redirect, url_for

from sql.db import DB

company = Blueprint('company', __name__, url_prefix='/company')


@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *
    # UCID=vr76, DATE=10/04/23
    query = "SELECT id, name, address, city, country, state, zip, website, (SELECT COUNT(*) FROM IS601_MP3_Employees WHERE company_id=companies.id) as employees FROM IS601_MP3_Companies companies"
    args = {}  # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    # UCID=vr76, DATE=10/04/23
    name = request.args.get('name', '')
    country = request.args.get('country', '')
    state = request.args.get('state', '')
    column = request.args.get('column', '')
    order = request.args.get('order', '')
    limit = request.args.get('limit', '')
    if name != '' or country != '' or state != '':
        query += " WHERE "
    # TODO search-3 append a LIKE filter for name if provided
    # UCID=vr76, DATE=10/04/23
    if name != '':
        name = f"%{name}%"
        args['name'] = name
        query += " name LIKE %(name)s"
    # TODO search-4 append an equality filter for country if provided
    # UCID=vr76, DATE=10/04/23
    if country != '':
        if list(query.split(" "))[-2] != 'WHERE':
            query += "AND"
        query += " country = %(country)s"
        args['country'] = country
    # TODO search-5 append an equality filter for state if provided
    # UCID=vr76, DATE=10/04/23
    if state != '':
        if list(query.split(" "))[-2] != 'WHERE':
            query += "AND"
        query += " state = %(state)s"
        args['state'] = state
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    # UCID=vr76, DATE=10/04/23
    if column != '':
        query += f" ORDER BY {column} {order}"
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # UCID=vr76, DATE=10/04/23
    if limit != '':
        limit = limit
    else:
        limit = 10
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    # UCID=vr76, DATE=10/04/23
    try:
        limit = int(limit)
    except:
        flash('Limit must be an integer', "danger")

    if limit < 1 or limit > 100:
        flash('Limit must be greater than 1 and less than or equal to 100', "danger")

    if column == '':
        query += f" ORDER BY id asc"

    # TODO change this per the above requirements
    if limit != '':
        limit = limit
    else:
        limit = 10
    query += " LIMIT %(limit)s"
    args["limit"] = limit
    print("query", query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user friendly
        # UCID=vr76, DATE=10/04/23
        flash("Something went wrong while getting company records", "danger")

    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    allowed_columns = [(v, v) for v in allowed_columns]
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)


@company.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        # UCID=vr76, DATE=10/04/23
        if 'name' in request.form:
            name = request.form['name']
        else:
            name = ""

        if 'address' in request.form:
            address = request.form['address']
        else:
            address = ""

        if 'city' in request.form:
            city = request.form['city']
        else:
            city = ""

        if 'state' in request.form:
            state = request.form['state']
        else:
            state = ""

        if 'country' in request.form:
            country = request.form['country']
        else:
            country = ""

        if 'zip' in request.form:
            zipcode = request.form['zip']
        else:
            zipcode = ""

        if 'website' in request.form:
            website = request.form['website']
        else:
            website = ""

        has_error = False  # use this to control whether or not an insert occurs
        # TODO add-2 name is required (flash proper error message)
        # UCID=vr76, DATE=10/04/23
        if name == "":
            flash('Company name required', "danger")
            has_error = True
        # TODO add-3 address is required (flash proper error message)
        # UCID=vr76, DATE=10/04/23
        if address == "":
            flash('Address is required', "danger")
            has_error = True
        # TODO add-4 city is required (flash proper error message)
        # UCID=vr76, DATE=10/04/23
        if city == "":
            flash('City is required', "danger")
            has_error = True
        # TODO add-5 state is required (flash proper error message)
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        # UCID=vr76, DATE=10/04/23
        if state == "":
            flash('State is required', "danger")
            has_error = True
        states = []
        if country.strip():
            states = pycountry.subdivisions.get(country_code=country.strip())
        if not states:
            states = []
        states = list(map(lambda s: {"name": s.name, "code": s.code.split("-")[1]}, states))
        states = [i['code'] for i in states]
        if state not in states:
            flash('State is not valid', "danger")
            has_error = True
        # TODO add-6 country is required (flash proper error message)
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        # UCID=vr76, DATE=10/04/23
        if country == "":
            flash('Country is required', "danger")
            has_error = True
        countries = list(map(lambda c: {"code": c.alpha_2, "name": c.name}, list(pycountry.countries)))
        countries = [i['code'] for i in countries]
        if country not in countries:
            flash('country is not valid', "danger")
            has_error = True
        # TODO add-7 website is not required
        # TODO add-8 zipcode is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        # UCID=vr76, DATE=10/04/23
        if zipcode == "":
            flash('zipcode is required', "danger")
            has_error = True

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Companies (name, address, city, country, state, zip, website)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, name, address, city, country, state, zipcode,
                                      website)  # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash("something went wrong while creating company record", "danger")

    return render_template("add_company.html")


@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    if request.args.get('id', '') == '':
        flash('id is required', "danger")

    id = request.args.get('id', '')
    if id != '':  # TODO update this for TODO edit-1
        data = {"id": id}  # use this as needed, can convert to tuple if necessary
        # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
        # UCID=vr76, DATE=10/04/23
        result = DB.selectOne(
            "SELECT id, name, address, city, country, state, zip, website, (SELECT COUNT(*) FROM IS601_MP3_Employees WHERE company_id=companies.id) as employee_count FROM IS601_MP3_Companies companies WHERE id=%s",
            id)
        if result.status:
            row = result.row
        has_error = False
        if 'name' in request.form:
            name = request.form['name']
        else:
            name = row['name']
            has_error = True

        if 'address' in request.form:
            address = request.form['address']
        else:
            address = row['address']
            has_error = True

        if 'city' in request.form:
            city = request.form['city']
        else:
            city = row['city']
            has_error = True

        if 'state' in request.form:
            state = request.form['state']
        else:
            state = row['state']
            has_error = True

        if 'country' in request.form:
            country = request.form['country']
        else:
            country = row['country']
            has_error = True

        if 'zip' in request.form:
            zipcode = request.form['zip']
        else:
            zipcode = row['zip']
            has_error = True

        if 'website' in request.form:
            website = request.form['website']
        else:
            website = row['website']
            # has_error = True

        # TODO edit-2 name is required (flash proper error message)
        # UCID=vr76, DATE=10/04/23
        if name == "":
            flash('Company name is required', "danger")
            has_error = True
        # TODO edit-3 address is required (flash proper error message)
        # UCID=vr76, DATE=10/04/23
        if address == "":
            flash('Address is required', "danger")
            has_error = True
        # TODO edit-4 city is required (flash proper error message)
        # UCID=vr76, DATE=10/04/23
        if city == "":
            flash('City is required', "danger")
            has_error = True
        # TODO edit-5 state is required (flash proper error message)
        # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        # UCID=vr76, DATE=10/04/23
        if state == "":
            flash('State is required', "danger")
            has_error = True
        states = []
        if country.strip():
            states = pycountry.subdivisions.get(country_code=country.strip())
        if not states:
            states = []
        states = list(map(lambda s: {"name": s.name, "code": s.code.split("-")[1]}, states))
        states = [i['code'] for i in states]
        if state not in states:
            flash('State is not valid', "danger")
            has_error = True
        # TODO edit-6 country is required (flash proper error message)
        # TODO edit-6a country should be a valid country mentioned in pycountry
        # UCID=vr76, DATE=10/04/23
        # hint see geography.py and pycountry documentation
        if country == "":
            flash('Country is required', "danger")
            has_error = True
        countries = list(map(lambda c: {"code": c.alpha_2, "name": c.name}, list(pycountry.countries)))
        countries = [i['code'] for i in countries]
        if country not in countries:
            flash('country is not valid', "danger")
            has_error = True
        # TODO edit-7 website is not required
        # UCID=vr76, DATE=10/04/23
        # TODO edit-8 zipcode is required (flash proper error message)

        if zipcode == "":
            flash('Country is required', "danger")
            has_error = True

        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        # populate data dict with mappings

        data["name"] = name
        data["address"] = address
        data["city"] = city
        data["state"] = state
        data["country"] = country
        data["zip"] = zipcode
        data["website"] = website
        if not has_error:
            try:
                # TODO edit-9 fill in proper update query
                # name, address, city, state, country, zip, website
                # UCID=vr76, DATE=10/04/23
                result = DB.update("""
                UPDATE IS601_MP3_Companies
                SET name=%(name)s, address=%(address)s, city=%(city)s, state=%(state)s, country=%(country)s, zip=%(zip)s, website=%(website)s WHERE id=%(id)s
                """, data)
                if result.status:
                    print("updated record")
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-10 make this user-friendly
                # UCID=vr76, DATE=10/04/23
                flash("There was an error updating the company record", "danger")
        row = {}
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne(
                "SELECT id, name, address, city, country, state, zip, website, (SELECT COUNT(*) FROM IS601_MP3_Employees WHERE company_id=companies.id) as employee_count FROM IS601_MP3_Companies companies WHERE id=%s",
                id)
            if result.status:
                row = result.row

        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash("There was an error retrieving the employee record", "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", company=row)


@company.route("/delete", methods=["GET"])
def delete():
    if request.args.get('id', '') == '':
        flash('id is required', "danger")

    id = request.args.get('id', '')
    # TODO delete-1 delete company by id (unallocate any employees see delete-5)
    try:
        pass
        employees_result = DB.update("""
                UPDATE IS601_MP3_Employees SET company_id=null WHERE company_id=%s
                """, id)

        result = DB.delete("DELETE FROM IS601_MP3_Companies WHERE id=%s", id)
        if result.status:
            # TODO delete-4 ensure a flash message shows for successful delete
            flash("Company record successfully deleted", "success")
    except Exception as e:
        print(str(e))
        flash("There was an error deleting company record", "danger")
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
    return redirect(url_for('company.search'))
