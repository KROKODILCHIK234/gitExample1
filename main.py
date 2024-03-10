from flask import Flask, request, Response
import csv
import json
import markdown2

app = Flask(__name__)

@app.route("/api/report/<storage_key>", methods=["GET"])
def get_report(storage_key: str):
    response_format = request.args.get('format', default='json')

    
    report_data = {
        "storage_key": storage_key,
        "some_data": "some_value"
    }

    if response_format == 'csv':
        
        with open("report.csv", 'w', newline='') as csvfile:
            csv_data = csv.DictWriter(csvfile, fieldnames=report_data.keys())
            csv_data.writeheader()
            csv_data.writerow(report_data)
        
        return Response(open("report.csv", 'r'), mimetype="text/csv")

    elif response_format == 'markdown':
       
        markdown_content = f"# Report\n\n- Storage Key: {report_data['storage_key']}\n- Some Data: {report_data['some_data']}"
        return Response(markdown2.markdown(markdown_content), mimetype="text/markdown")

    else:
        
        return json.dumps(report_data), 200, {'Content-Type': 'application/json'}

if __name__ == "__main__":
    app.run(debug=True)
