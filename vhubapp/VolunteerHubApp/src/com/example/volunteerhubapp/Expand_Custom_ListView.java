package com.example.volunteerhubapp;

import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.actionbarsherlock.app.SherlockActivity;
import com.boopathy.raja.tutorial.R;

public class Expand_Custom_ListView extends SherlockActivity 
{
	@Override
	protected void onCreate(Bundle savedInstanceState) 
	{
		super.onCreate(savedInstanceState);
		this.setTitle("Custom Expandable ListView");
		setContentView(R.layout.listview_custom_expand_layout);

		ListView list = (ListView) findViewById(R.id.listview_custom_expand);

		ArrayAdapter<String> listAdapter = new CustomListAdapter(this, R.layout.listview_custom_expand_item);
		for (int i = 0; i < 20; i++)
			listAdapter.add("Demo " + i);
		list.setAdapter(listAdapter);

		list.setOnItemClickListener(new AdapterView.OnItemClickListener()
		{
			public void onItemClick(AdapterView<?> parent, final View view, int position, long id) 
			{
				View toolbar = view.findViewById(R.id.listview_toolbar);
				Expand_Custom_Animation expandAni = new Expand_Custom_Animation(toolbar, 500);
				toolbar.startAnimation(expandAni);
				
				Button a = (Button) view.findViewById(R.id.list_do1);
				a.setOnClickListener(new OnClickListener() 
				{				
					@Override
					public void onClick(View v) 
					{
						Toast.makeText(getApplicationContext(), "Toast 1", Toast.LENGTH_SHORT).show();
					}
				});
				
				Button b = (Button) view.findViewById(R.id.list_do2);
				b.setOnClickListener(new OnClickListener() 
				{				
					@Override
					public void onClick(View v) 
					{
						Toast.makeText(getApplicationContext(), "Toast 2", Toast.LENGTH_SHORT).show();
					}
				});
			}
		});
	}

	class CustomListAdapter extends ArrayAdapter<String> 
	{
		public CustomListAdapter(Context context, int textViewResourceId) 
		{
			super(context, textViewResourceId);
		}

		@Override
		public View getView(int position, View convertView, ViewGroup parent) 
		{
			if (convertView == null) 
			{
				convertView = getLayoutInflater().inflate(R.layout.listview_custom_expand_item, null);
			}
			((TextView) convertView.findViewById(R.id.listview_title)).setText(getItem(position));

			View toolbar = convertView.findViewById(R.id.listview_toolbar);
			((LinearLayout.LayoutParams) toolbar.getLayoutParams()).bottomMargin = -50;
			toolbar.setVisibility(View.GONE);
			return convertView;
		}
	}
}
