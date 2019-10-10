package id.plant.plantiddemo;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.util.Base64;
import android.util.Log;
import android.widget.Toast;
import com.android.volley.DefaultRetryPolicy;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONTokener;

import java.io.ByteArrayOutputStream;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Backend {
    private static final String SERVER_URL = "https://api.plant.id";
    private static final String API_KEY = "yourApiKey";
    private static final int UPLOAD_IMAGE_SIZE = 1024;
    private Context context;
    static private MainActivity activity;

    private final RequestQueue queue;


    Backend(MainActivity mainActivity) {
        activity = mainActivity;
        context = mainActivity;
        queue = Volley.newRequestQueue(context);
    }

    /* call identification API endpoint */
    void identify(final List<String> imagePaths){
        String url = SERVER_URL + "/identify";

        StringRequest request = new StringRequest(com.android.volley.Request.Method.POST, url,
            new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    try {
                        JSONObject json = new JSONObject(new JSONTokener(response));
                        Log.d("identification", json.toString());
                        // report back to activity ID of new identification
                        activity.addIdentification(json.getInt("id"));
                    } catch (JSONException error) {
                        error.printStackTrace();
                    }
                }
            },
            new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                    Toast.makeText(context, "Upload failed", Toast.LENGTH_SHORT).show();
                    try {
                        Log.e("backedResponse", new String(error.networkResponse.data, "utf-8"));
                    } catch (UnsupportedEncodingException e) {
                        e.printStackTrace();
                    }
                }
            }
        ) {
            /* define POST parameters */
            @Override
            protected Map<String, String> getParams(){
                Map<String, String> params = new HashMap<>();

                JSONObject data = new JSONObject();
                JSONArray images = new JSONArray();
                for (String imagePath: imagePaths){
                    Bitmap bitmap = decodeSampledBitmapFromPath(imagePath, UPLOAD_IMAGE_SIZE, UPLOAD_IMAGE_SIZE);
                    images.put(getStringImage(bitmap));
                }

                try {
                    data.put("key", API_KEY);
                    data.put("images", images);
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                params.put("data", data.toString());
                return params;
            }
        };

        request.setRetryPolicy(new DefaultRetryPolicy(30 * 1000, 0, DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
        queue.add(request);
    }

    /* check whether identification is completed and retrieve results */
    void checkIdentification(final int id) {
        String url = SERVER_URL + "/check_identifications";
        StringRequest request = new StringRequest(com.android.volley.Request.Method.POST, url,
            new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    Log.d("check", response);
                    try {
                        JSONObject json = new JSONArray(new JSONTokener(response)).getJSONObject(0);
                        JSONArray suggestions = json.getJSONArray("suggestions");

                        List<String> suggestionPlantNames = new ArrayList<>();
                        if (suggestions.length() > 0){
                            for (int i = 0; i < suggestions.length(); i++) {
                                suggestionPlantNames.add(suggestions.getJSONObject(i).getJSONObject("plant").getString("name"));
                            }
                            // report back to activity plant suggestions
                            activity.addIdentificationResult(suggestionPlantNames);
                        }
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
            },
            new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                }
            }
        ) {
            @Override
            protected Map<String, String> getParams(){
                Map<String, String> params = new HashMap<>();

                JSONObject data = new JSONObject();
                JSONArray ids = new JSONArray();
                ids.put(id);

                try {
                    data.put("key", API_KEY);
                    data.put("ids", ids);
                } catch (JSONException error) {
                    error.printStackTrace();
                }

                params.put("data", data.toString());
                return params;
            }
        };
        queue.add(request);
    }

    /* get base64 image data from bitmap */
    private static String getStringImage(Bitmap bitmap){
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        bitmap.compress(Bitmap.CompressFormat.JPEG, 100, bos);
        byte[] imageBytes = bos.toByteArray();

        return Base64.encodeToString(imageBytes, Base64.DEFAULT);
    }

    /* load image from file with suitable size */
    private static Bitmap decodeSampledBitmapFromPath(String path, int reqWidth, int reqHeight) {
        final BitmapFactory.Options options = new BitmapFactory.Options();
        options.inJustDecodeBounds = true;
        BitmapFactory.decodeFile(path, options);
        options.inSampleSize = calculateInSampleSize(options, reqWidth, reqHeight);
        options.inJustDecodeBounds = false;
        Bitmap bitmap = BitmapFactory.decodeFile(path, options);
        return bitmap;
    }

    /* compute sampling size from image and required size */
    private static int calculateInSampleSize(BitmapFactory.Options options, int reqWidth, int reqHeight) {
        // Raw height and width of image
        final int height = options.outHeight;
        final int width = options.outWidth;
        int inSampleSize = 1;

        if (height > reqHeight || width > reqWidth) {
            final int halfHeight = height / 2;
            final int halfWidth = width / 2;
            // Calculate the largest inSampleSize value that is a power of 2 and keeps both
            // height and width larger than the requested height and width.
            while ((halfHeight / inSampleSize) >= reqHeight && (halfWidth / inSampleSize) >= reqWidth) {
                inSampleSize *= 2;
            }
        }

        return inSampleSize;
    }

}
