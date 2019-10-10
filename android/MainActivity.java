package id.plant.plantiddemo;

import android.Manifest;
import android.app.Activity;
import android.content.ClipData;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.provider.MediaStore;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private static final int REQUEST_PHOTO_FROM_GALLERY = 0;
    private static final int REQUEST_PERMISSIONS = 666;

    private List<String> images = new ArrayList<>();
    private Backend backend;
    private int identificationId;

    private Handler handler = new Handler();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if (ActivityCompat.checkSelfPermission(MainActivity.this, Manifest.permission.READ_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(MainActivity.this, new String[]{Manifest.permission.READ_EXTERNAL_STORAGE, Manifest.permission.WRITE_EXTERNAL_STORAGE}, REQUEST_PERMISSIONS);
        }

        backend = new Backend(this);
        getImagesFromGallery();
    }

    private void getImagesFromGallery() {
        Intent photoPickerIntent = new Intent(Intent.ACTION_PICK, android.provider.MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
        if (android.os.Build.VERSION.SDK_INT >= 18){
            photoPickerIntent.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, true);
        }
        startActivityForResult(photoPickerIntent, MainActivity.REQUEST_PHOTO_FROM_GALLERY);
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (resultCode == Activity.RESULT_OK && requestCode == MainActivity.REQUEST_PHOTO_FROM_GALLERY) {
            if (android.os.Build.VERSION.SDK_INT >= 18 && data.getClipData() != null) {
                ClipData clipdata = data.getClipData();
                for (int i = 0; i < clipdata.getItemCount(); i++) {
                    addImage(clipdata.getItemAt(i).getUri());
                }
            } else {
                addImage(data.getData());
            }
        }

        backend.identify(images);
    }

    private void addImage(Uri uri) {
        String path = null;
        String[] proj = { MediaStore.Images.Media.DATA };
        Cursor cursor = getContentResolver( ).query( uri, proj, null, null, null );
        if(cursor != null){
            if ( cursor.moveToFirst( ) ) {
                int column_index = cursor.getColumnIndexOrThrow( proj[0] );
                path = cursor.getString( column_index );
            }
            cursor.close( );
        }

        Log.i("image", path);
        images.add(path);
    }

    /* process new identification */
    void addIdentification(int id) {
        identificationId = id;
        handler.post(checkIdentification);  // start periodic check of identification result
    }

    /* process identification result */
    void addIdentificationResult(List<String> suggestions) {
        handler.removeCallbacks(checkIdentification);  // stop periodic check

        for (String suggestion: suggestions){
            Log.d("suggestion", suggestion);
        }
    }

    /* task for periodic check of identification */
    private Runnable checkIdentification = new Runnable() {
        @Override
        public void run() {
            backend.checkIdentification(identificationId);
            handler.postDelayed(this, 3000);
        }
    };

}
