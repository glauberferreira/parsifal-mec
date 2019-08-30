# coding: utf-8

from django.conf.urls import patterns, include, url


urlpatterns = patterns('parsifal.reviews.planning.views',
    url(r'^save_source/$', 'save_source', name='save_source'),
    url(r'^remove_source/$', 'remove_source_from_review', name='remove_source_from_review'),
    url(r'^suggested_sources/$', 'suggested_sources', name='suggested_sources'),
    url(r'^add_suggested_sources/$', 'add_suggested_sources', name='add_suggested_sources'),
    url(r'^save_question/$', 'save_question', name='save_question'),
    url(r'^save_question_order/$', 'save_question_order', name='save_question_order'),
    url(r'^save_picoc/$', 'save_picoc', name='save_picoc'),
    url(r'^add_or_edit_question/$', 'add_or_edit_question', name='add_or_edit_question'),
    url(r'^remove_question/$', 'remove_question', name='remove_question'),
    url(r'^save_objective/$', 'save_objective', name='save_objective'),
    url(r'^add_criteria/$', 'add_criteria', name='add_criteria'),
    url(r'^remove_criteria/$', 'remove_criteria', name='remove_criteria'),
    url(r'^save_selection_reviewer/$', 'save_selection_reviewer', name='save_selection_reviewer'),

    url(r'^save_risk/$', 'save_risk', name='save_risk'),
    url(r'^save_risk_order/$', 'save_risk_order', name='save_risk_order'),
    url(r'^remove_risk/$', 'remove_risk', name='remove_risk'),
    url(r'^add_or_edit_risk/$', 'add_or_edit_risk', name='add_or_edit_risk'),
    url(r'^suggested_risks/$', 'suggested_risks', name='suggested_risks'),
    url(r'^share_risks/$', 'share_risks', name='share_risks'),
    url(r'^save_statistical_methods/$', 'save_statistical_methods', name='save_statistical_methods'),
    
    


    url(r'^import_pico_keywords/$', 'import_pico_keywords', name='import_pico_keywords'),
    url(r'^add_keyword/$', 'add_keyword', name='add_keyword'),
    url(r'^edit_keyword/$', 'edit_keyword', name='edit_keyword'),
    url(r'^remove_keyword/$', 'remove_keyword', name='remove_keyword'),

    url(r'^add_quality_assessment_question/$', 'add_quality_assessment_question', name='add_quality_assessment_question'),
    url(r'^edit_quality_assessment_question/$', 'edit_quality_assessment_question', name='edit_quality_assessment_question'),
    url(r'^save_quality_assessment_question/$', 'save_quality_assessment_question', name='save_quality_assessment_question'),
    url(r'^save_quality_assessment_question_order/$', 'save_quality_assessment_question_order', name='save_quality_assessment_question_order'),
    url(r'^remove_quality_assessment_question/$', 'remove_quality_assessment_question', name='remove_quality_assessment_question'),
    url(r'^suggested_quality_assessment_questions/$', 'suggested_quality_assessment_questions', name='suggested_quality_assessment_questions'),
    url(r'^share_quality_assessment_questions/$', 'share_quality_assessment_questions', name='share_quality_assessment_questions'),
    url(r'^add_quality_assessment_answer/$', 'add_quality_assessment_answer', name='add_quality_assessment_answer'),
    url(r'^edit_quality_assessment_answer/$', 'edit_quality_assessment_answer', name='edit_quality_assessment_answer'),
    url(r'^save_quality_assessment_answer/$', 'save_quality_assessment_answer', name='save_quality_assessment_answer'),
    url(r'^remove_quality_assessment_answer/$', 'remove_quality_assessment_answer', name='remove_quality_assessment_answer'),
    url(r'^suggested_quality_assessment_answers/$', 'suggested_quality_assessment_answers', name='suggested_quality_assessment_answers'),
    url(r'^add_suggested_answer/$', 'add_suggested_answer', name='add_suggested_answer'),
    url(r'^add_new_data_extraction_field/$', 'add_new_data_extraction_field', name='add_new_data_extraction_field'),
    url(r'^edit_data_extraction_field/$', 'edit_data_extraction_field', name='edit_data_extraction_field'),
    url(r'^save_data_extraction_field/$', 'save_data_extraction_field', name='save_data_extraction_field'),
    url(r'^save_data_extraction_field_order/$', 'save_data_extraction_field_order', name='save_data_extraction_field_order'),
    url(r'^remove_data_extraction_field/$', 'remove_data_extraction_field', name='remove_data_extraction_field'),
    url(r'^suggested_data_extraction_fields/$', 'suggested_data_extraction_fields', name='suggested_data_extraction_fields'),
    url(r'^share_data_extraction_fields/$', 'share_data_extraction_fields', name='share_data_extraction_fields'),
    url(r'^calculate_max_score/$', 'calculate_max_score', name='calculate_max_score'),
    url(r'^save_cutoff_score/$', 'save_cutoff_score', name='save_cutoff_score'),
    url(r'^generate_search_string/$', 'generate_search_string', name='generate_search_string'),
    url(r'^save_generic_search_string/$', 'save_generic_search_string', name='save_generic_search_string'),
    
    url(r'^setting_pico/$', 'setting_pico', name='setting_pico'),
)
